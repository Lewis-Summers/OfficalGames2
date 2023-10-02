from django.db import models
from user.models import User
from django.utils import timezone


genderChoices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Coed'),
)


# Step 1: Tables without foreign key references
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    leadAdmin = models.ForeignKey(User, on_delete=models.CASCADE)
    accessCode = models.CharField(max_length=5, null=True)
    # paymentHistory = models.JSONField()

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    # sport

# Step 2: Tables with foreign key references to tables created in Step 1
class Sport(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Complex(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Age(models.Model):
    title = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

class Leagues(models.Model):
    name = models.CharField(max_length=255)
    rule_set = models.TextField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    def payValue(self, assignment):
        game = assignment.game
        age = game.age  # Assuming age information is associated with the home team
        gender = game.gender  # Assuming gender information is associated with the home team
        # Find the relevant PayScale based on sport, age, and gender
        try:
            pay_scale = PayScale.objects.get(
                league=self,
                role=assignment.role,
                age=age,
                gender=gender
            )
            return pay_scale
        except PayScale.DoesNotExist:
            return None

class Teams(models.Model):
    team_name = models.CharField(max_length=255)
    player_list_dict = models.TextField()
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)

class Field(models.Model):
    name = models.CharField(max_length=255)
    complex = models.ForeignKey(Complex, on_delete=models.CASCADE)

class Notification(models.Model):
    text = models.TextField()
    admin = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


# Step 3: Tables with foreign key references to tables created in Steps 1 and 2
class Game(models.Model):
    assigned_game_id = models.IntegerField(blank=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=2, choices=genderChoices, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, null=True)
    home_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='home_games', null=True)
    away_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='away_games', null=True)
    home_score = models.IntegerField(null=True)
    away_score = models.IntegerField(null=True)
    date_time = models.DateTimeField(null=True)
    admin_notes = models.TextField(null=True)
    game_report = models.TextField(null=True) # gonna have to move to game assingments
    needs_admin = models.BooleanField(null=True)
    
    def happened(self):
        if self.date_time is not None:
            return self.date_time <= timezone.now()
        return False



class PayScale(models.Model):
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    numRef = models.IntegerField()
    gender = models.CharField(max_length=2, choices=genderChoices)


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    CHOICES = (
        ('A', 'Accepted'),
        ('D', 'Declined'),
        ('P', 'Pending'),
    )
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    status = models.CharField(max_length=2, choices=CHOICES, default='P')
    paid = models.BooleanField(default=False)
    payApproved = models.BooleanField(default=False)
    # game report
    # needs admin review


class CompanyMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    isAdmin = models.BooleanField(default=False, null=True, blank=True)
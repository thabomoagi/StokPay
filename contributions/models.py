from django.db import models


class Stokvel(models.Model):
    name = models.CharField(max_length=100)
    contribution_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payout_day = models.IntegerField(help_text="Day of month payouts happen")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    stokvel = models.ForeignKey(Stokvel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contribution(models.Model):
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('missed', 'Missed'),
        ('late', 'Late'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='paid')

    def __str__(self):
        return f"{self.member.name} - R{self.amount} ({self.status})"


class Payout(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('skipped', 'Skipped'),
    ]
    stokvel = models.ForeignKey(Stokvel, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.member.name} - R{self.amount} ({self.status})"

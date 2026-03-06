from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - R{self.amount}"

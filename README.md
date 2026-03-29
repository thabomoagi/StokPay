# StokPay

Stokvels run this country. R50 billion a year, 11 million members and most of it still tracked on WhatsApp chats and paper. That's the problem StokPay is solving.

This is a platform that gives stokvel groups a proper home track contributions, schedule payouts, see who's paid and who hasn't, all in one place. No more "uSbongile did you pay this month?" drama in the group chat.

## What it does right now
- Create and manage multiple stokvel groups
- Add members and link them to their group
- Record contributions, mark them paid, missed or late
- Schedule payouts and track who's received the pot
- Each member has a live balance showing exactly what they've contributed
- Secure login so only your group's admins can access the data
- Clean dashboard to see everything at a glance

## Coming soon
- WhatsApp notifications, reminders when contributions are due, alerts when payouts drop
- Stokvel summary view, total pot, total paid out, who's next in line
- Mobile friendly
- Live deployment so groups can access it anywhere

## Stack
Django · Django REST Framework · JWT Auth · SQLite · Docker

## Run it locally
```bash
git clone https://github.com/thabomoagi/StokPay.git
cd StokPay
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000` and sign in.

## Built by
Thabo Moagi — Johannesburg 🇿🇦
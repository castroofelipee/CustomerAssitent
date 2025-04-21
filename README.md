# French Laudure – Morning Huddle Tool

A streamlined internal tool built to support **fine-dining restaurant staff** during their daily morning huddles — ensuring personalized, efficient, and high-quality service through automated reservation insights.

---

## The Challenge

Build an end-to-end product experience for French Laudure's daily **morning huddle**, focused on either **front-of-house (FoH)** or **back-of-house (BoH)** staff.

This tool automates the review of:

- Daily reservations
- Guest insights (VIPs, allergies, special occasions)
- Priority service flows

The goal: to align staff around exceptional service delivery.

---

## My Approach

I chose to focus on the **Front-of-House (FoH)** team — helping hosts and waitstaff personalize interactions and prioritize key guests for the day.

The tool includes:

- ✅ List of all reservations for the day
- ✅ Highlights dietary restrictions, VIP status, and special occasions
- ✅ Quick glance UX for prioritizing attention and service roles
- ✅ Clear and maintainable codebase (React + Tailwind + FastAPI)

---

## Tech Stack

| Layer         | Tech Used            |
|---------------|----------------------|
| Frontend      | React + Tailwind CSS |
| Backend       | FastAPI              |
| Language Model| OpenAI GPT (planning, prompt-saving) |
| Dev Tools     | Docker, LazyVim, Git |
| Dataset       | Provided JSON dataset (`/data/reservations.json`) |

---


## Get started
```cd Frontend
```

after that:

```
npm install && npm run Dev
```
You be able to see frontend service in `localhost:3000`

for the best experience, run the backend service:

```
cd backend && poestry install --no-root
```
set the poetry shell

``` 
poetry shell
``` 

and:

```
uvicorn main:app --reload
```

The frontend will fetch the reservations from `localhost:8000/reservations` and also can see the swagger docs in `/docs`
```
```
```
```
```
```
```
```
```
```

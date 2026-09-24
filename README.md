# RAIN 🌧️

A cloud-based, serverless telemedicine platform built for the AWS Student Builder Club Hackathon at SRIT — placed **Top 4**, awarded the **Consolation Prize**.

🔗 **Live demo:** http://rain-telemed-site.s3-website.ap-south-1.amazonaws.com

---

## What it does

Rain lets patients register, get an AI-assisted specialist suggestion based on their symptoms, book appointments with real-time conflict checking, join live video consultations, securely upload medical reports, receive digital prescriptions, and view their full medical history — all without a single server being manually managed.

**Core flow:** Register → Check symptoms → Book appointment → Consult a doctor → Upload report → Digital prescription → View history

## Tech stack

| Service | Role |
|---|---|
| **AWS Lambda** | Backend logic — one function per action (register, book, upload, prescribe, suggest specialty, fetch history) |
| **Amazon API Gateway** | Exposes each Lambda function as a secure HTTPS endpoint |
| **Amazon DynamoDB** | NoSQL database — patients, appointments, and reports tables |
| **Amazon S3** | Stores uploaded medical reports privately, and hosts the frontend itself as a static website |
| **Amazon Bedrock** | AI symptom-to-specialist suggestion, architected for Claude; currently running a rule-based fallback due to a sandbox account billing restriction — the Bedrock integration code is written and ready to activate |
| **Jitsi Meet** | Real, working video consultation rooms generated per appointment |

## Features

- 🩺 Patient registration with short, readable IDs (`PAT-XXXXXX`)
- 🤖 AI-assisted symptom checker suggesting a specialist
- 📅 Appointment booking with double-booking prevention per doctor
- 🎥 Live video consultations
- 📄 Secure medical report uploads to S3
- 💊 Digital prescriptions tied to appointments
- 📖 Full patient history view (past appointments + reports)
- 🌗 Dark/light theme toggle
- 🔁 Auto-remembered patient/appointment IDs across the session — no manual copy-pasting

## What I'd add next

- **Amazon Cognito** for real authentication instead of ID-based access
- **Amazon SNS** for appointment confirmation emails/SMS
- Doctor-side dashboard to view and manage bookings
- Presigned S3 URLs so doctors can view uploaded reports in-app
- IAM least-privilege scoping (currently using broader permissions for hackathon speed)

## Background

Built from zero prior AWS experience in roughly 5 hours during a hackathon — the workshop, the build, and a live debugging session (including a CORS configuration issue resolved minutes before the final presentation) are all part of the story.

---

Built by [Vennela R](https://github.com/vennelar11) 
Read more at [Medium](https://medium.com/@vennelareddyvari.11)

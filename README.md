# 🌐 Disaster Response API

A simple Flask-based REST API that provides disaster safety tips, emergency numbers, safe zones, and map links.  
Supports both **GET** and **POST** requests, tested using Postman.

---

## 🚀 Features
- Get disaster safety information using:
  - Path parameter → `/fire`
  - Query parameter → `?disaster=flood`
  - POST request with JSON body
- Returns structured JSON response:
  - Safety message
  - Emergency contact numbers
  - Nearby safe zones
  - Google Maps link
  - Timestamp

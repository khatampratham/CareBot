## Objective ##
AI for healthcare monitoring: fall detection, patient activity tracking, and alerts.

## Tech Stack ##
- Python 3.11
- motion detection algo

## features ##
- detects unsual activities in elders
- sends alerts to emergency contacts and caregivers
- 24x7 patient monitoring

## how to run ## 
1. `cd 10-carebot` in cmd 
2. Create venv:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
3. download requirements
   ```powershell
   python -m pip install -r requirements.txt
4. run the server
   ```powershell
   uvicorn app.main:app --reload --port 8009
5. try testing with `/wrte` for the endpoint:
   ```powershell
   $headers = @{ "Content-Type" = "application/json" }
   $body = '{"topic":"AI in healthcare","style":"professional"}'
   Invoke-WebRequest -Uri "http://127.0.0.1:8009/write" -Method POST -Headers $headers -Body $body


NOTE: TO upgrade further can be extended with real time camera feeds.


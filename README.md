# Smart Waste Segregation Assistant

An AI-powered sustainability assistant to guide users on proper waste disposal.

## Features
- Text-based waste classification
- Disposal instructions
- Sustainability tips

## Setup Instructions
1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run server:
   python app.py

## API Usage
POST /predict

Request body:
{
  "item": "banana peel"
}

Response:
{
  "category": "wet_waste",
  "instruction": "Place in green bin or compost.",
  "tip": "Composting reduces methane emissions."
}

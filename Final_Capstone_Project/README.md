# Dynamic Pricing for Urban Parking Lots

Capstone Project – **Summer Analytics 2025**
Hosted by: Consulting & Analytics Club and Pathway

# Problem Statement

Urban parking spaces are a limited and highly demanded resource. Prices that remain static
throughout the day can lead to inefficiencies — either overuse or underuse.
To improve utilization, dynamic pricing based on demand, competition, and real-time
conditions is crucial.

The objective is to:

- Dynamically adjust parking prices in real time using vehicle, traffic and lot data starting from a base of *$10*
- Use only **Python, Pandas, Numpy and Pathway**
- Visualize pricing behavior in real time using *Bokeh*


# Tech Stack

- **Language**: Python  
- **Libraries**: 
  - pandas – for data manipulation  
  - numpy – for numerical operations  
- **Streaming & Real-Time Processing**: 
  - Pathway – to simulate real time data  
- **Visualization**: 
  - bokeh – for real time interactive plotting  
- **Data Structures**: 
  - Pathway Tables  
  - Pandas DataFrames
- **Environment**: 
  - Google Colab – for code execution



# Dataset Description

- **Duration**: 73 days  
- **Time points**: 18 per day (every 30 minutes from 8:00 AM to 4:30 PM)  
- **Parking lots**: 14

**Features include:**
- **Location**: Latitude and Longitude of parking slots
- **Capacity & Occupancy**
- **Queue length**
- **Traffic level**
- **Special day indicator**
- **Incoming vehicle type** (car, bike, truck)



## 🧠 Modules Implemented

# Module 1: Baseline Linear Model
- Price is updated linearly with occupancy:
- Assumption: Price starts with $10 every day


# Module 2: Demand Based Pricing

A demand function is created using:
- Occupancy rate
- Queue length
- Traffic level
- Special day
- Vehicle type


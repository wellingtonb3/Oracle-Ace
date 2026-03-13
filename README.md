# Oracle-Ace
Oracle Ace Program for OCI Certified


# IoT Edge-to-Cloud: Real-Time Monitoring with OCI

![OCI Realtime](https://raw.githubusercontent.com/wellingtonb3/Oracle-Ace/main/images/OCI%20Realtime.png)


## 📌 Project Overview

This project demonstrates a low-cost, scalable end-to-end IoT solution designed for agricultural intelligence and environmental security. By leveraging **MicroPython** on an **ESP32** and the power of **Oracle Cloud Infrastructure (OCI)**, I have created a system that monitors environmental data in real-time, providing high-quality data ingestion into an **Oracle Autonomous Database**.

As an **OCI Certified professional**, I designed this architecture to prove that enterprise-grade cloud tools can be seamlessly integrated with edge computing for high-performance results.

![Swimming Pool](https://raw.githubusercontent.com/wellingtonb3/Oracle-Ace/main/images/Swimming%20pool.png)
---

## 🚀 Key Features

* **Edge Computing:** ESP32 programmed with MicroPython for efficient data handling.
* **Real-Time Data Ingestion:** Automated data transmission every 60 seconds via secure REST APIs.
* **Cloud Infrastructure:** Built on **Oracle Autonomous Data Warehouse (ADW)** (Free Tier).
* **Scalable Design:** Hardware-agnostic logic that supports temperature, humidity, vibration, presence, and water level sensors.
* **AI-Ready:** Project documentation and logic optimization assisted by **Gemini** and **NotebookLM**.

---

## 🛠 Technical Architecture

The system follows a 3-tier architecture:

1. **Edge Layer:** ESP32 (Station) collects sensor data and connects via Wi-Fi.
2. **Transport Layer:** Data is sent via HTTPS/REST to the OCI gateway.
3. **Cloud Layer:** Oracle Autonomous Database stores and organizes the data for real-time analysis and dashboarding.

---

## 📂 Repository Structure

* `/src`: Contains the `main.py` and configuration files for the ESP32 (MicroPython).
* `/sql`: Database schema and initialization scripts for Oracle ADW.
* `/docs`: Technical diagrams and project illustrations.
* `/notebooks`: Data analysis exports and visualization logic.

---

## 💡 How to Use

1. **Configure OCI:** Set up your Autonomous Database and obtain your OCI Wallet or REST Endpoint.
2. **Flash ESP32:** Install MicroPython on your ESP32 board.
3. **Deploy Code:** Update `config.py` with your Wi-Fi credentials and OCI details, then upload the `/src` files.
4. **Monitor:** Access your OCI Console to view real-time data flowing into your tables.

---

## 🏆 Oracle ACE Apprentice Milestone

This project is part of my journey in the **Oracle ACE Program**. It reflects the practical application of my **OCI Certification** and my commitment to sharing cloud knowledge with the developer community.

---

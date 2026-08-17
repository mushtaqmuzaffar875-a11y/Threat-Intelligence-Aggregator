# 🛡️ Threat Intelligence Aggregator

A Python-based threat intelligence aggregation tool designed to collect, normalize, validate, deduplicate, and report Indicators of Compromise (IOCs) in authorized cybersecurity and educational environments.

## 👨‍💻 Author

MUZAFFAR MUSHTAQ

Cybersecurity Aspirant

## 🔍 Features

- IOC collection and aggregation
- IP address detection
- Domain detection
- URL detection
- MD5 hash detection
- SHA1 hash detection
- SHA256 hash detection
- IOC normalization
- IOC validation
- Duplicate IOC detection
- Threat intelligence statistics
- JSON report generation
- Automated unit testing
- Safe synthetic sample feed

## 🧩 Supported IOC Types

The aggregator currently supports:

- IPv4 addresses
- Domains
- HTTP/HTTPS URLs
- MD5 hashes
- SHA1 hashes
- SHA256 hashes

## ⚠️ Security Notice

This project is intended for:

- Educational purposes
- Cybersecurity learning
- Security research
- Authorized security testing
- Threat intelligence demonstrations

The included sample indicators are synthetic or documentation-only examples.

Do not use this project to interact with or investigate systems without proper authorization.

## 📋 Requirements

- Python 3
- Linux / Kali Linux
- Python standard library

No external Python packages are required for the current version.

## 🚀 Installation

Clone the repository:

git clone https://github.com/mushtaqmuzaffar875-a11y/Threat-Intelligence-Aggregator.git

cd Threat-Intelligence-Aggregator

## ▶️ Usage

Run the aggregator:

python3 main.py

The application loads the safe sample threat-intelligence feed, validates the indicators, removes duplicates, displays statistics, and generates a JSON report.

## 📊 Example Output

Total Valid IOCs: 10

IOC Statistics:

DOMAIN : 2
IP : 3
MD5 : 1
SHA1 : 1
SHA256 : 1
URL : 2

The generated report is saved as:

reports/threat_intelligence_report.json

## 🧪 Testing

Run the complete test suite:

python3 -m unittest discover -s tests -v

The project includes tests for:

- IP detection
- Domain detection
- URL detection
- Hash detection
- IOC validation
- IOC normalization
- Duplicate detection
- IOC statistics
- Indicator aggregation

## 📁 Project Structure

Threat-Intelligence-Aggregator/
├── core/
│   ├── __init__.py
│   ├── aggregator.py
│   ├── normalizer.py
│   └── validator.py
├── data/
├── reports/
│   ├── __init__.py
│   └── report_generator.py
├── sources/
│   ├── __init__.py
│   └── sample_feed.py
├── tests/
│   ├── __init__.py
│   └── test_aggregator.py
├── config.py
├── main.py
├── README.md
├── LICENSE
└── .gitignore

## 📄 JSON Reports

The application generates structured JSON reports containing:

- Report title
- Author
- Generation timestamp
- Total indicators
- IOC statistics
- Indicator values
- IOC types
- Threat-intelligence source

## 🎯 Educational Goals

This project demonstrates practical cybersecurity concepts including:

- Threat intelligence
- Indicators of Compromise (IOCs)
- Data normalization
- Input validation
- Deduplication
- Security automation
- JSON reporting
- Python programming
- Automated testing

## 🔮 Future Improvements

- Additional IOC formats
- CSV feed support
- STIX/TAXII integration
- Multiple threat-intelligence sources
- Confidence scoring
- IOC reputation scoring
- CSV and HTML reports
- Configurable feed sources
- Scheduled feed updates
- Database storage

## 📄 License

MIT License

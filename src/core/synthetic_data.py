"""
CrimeLens - Synthetic Data Engine
Interconnected datasets engineered for investigation intelligence, entity resolution,
and cross-case link discovery.
"""

DEMO_CASES = [
    {
        "case_id": "FIR-104",
        "title": "Vehicle & Electronic Goods Theft",
        "date": "2026-08-12",
        "location": "Kothrud, Pune",
        "station": "Kothrud Police Station",
        "io_name": "PI Vikram Patil",
        "io_badge": "MH-PN-4082",
        "status": "ACTIVE",
        "priority": "HIGH",
        "description": "High-value theft of white sedan and commercial IT equipment from commercial complex parking lot.",
        "entities_count": 18,
        "relations_count": 32,
        "evidence_count": 14,
        "alerts_count": 3
    },
    {
        "case_id": "FIR-087",
        "title": "Commercial Warehouse Burglary",
        "date": "2026-08-10",
        "location": "Swargate, Pune",
        "station": "Swargate Police Station",
        "io_name": "API Sneha Deshmukh",
        "io_badge": "MH-PN-3319",
        "status": "ACTIVE",
        "priority": "MEDIUM",
        "description": "Forced nighttime entry into electronics distributor warehouse. Getaway vehicle observed on CCTV.",
        "entities_count": 14,
        "relations_count": 24,
        "evidence_count": 11,
        "alerts_count": 2
    },
    {
        "case_id": "FIR-052",
        "title": "Corporate Cyber Extortion & Money Laundering",
        "date": "2026-07-28",
        "location": "Hinjawadi, Pune",
        "station": "Cyber Crime Police Station",
        "io_name": "ACP Rohan Kulkarni",
        "io_badge": "MH-PN-1102",
        "status": "IN REVIEW",
        "priority": "HIGH",
        "description": "Ransomware extortion demanding payment routed through mule accounts and local shell conduits.",
        "entities_count": 22,
        "relations_count": 41,
        "evidence_count": 19,
        "alerts_count": 4
    }
]

DEMO_ENTITIES = [
    {
        "id": "ENT-001",
        "name": "Rahul Sharma",
        "type": "PERSON",
        "aliases": ["Rahul Sharm", "R. Sharma"],
        "phone": "+91 98765 43210",
        "vehicle": "MH12AB1234",
        "location": "Kothrud, Pune",
        "priority_score": 87,
        "priority_level": "HIGH",
        "cases": ["FIR-104", "FIR-087"],
        "details": {
            "age": 32,
            "priors": 3,
            "gang": "Pune Local Syndicate",
            "occupation": "Automobile Broker (Suspected Fence)"
        }
    },
    {
        "id": "ENT-002",
        "name": "Amit Verma",
        "type": "PERSON",
        "aliases": ["Amit V."],
        "phone": "+91 98230 11223",
        "vehicle": "MH14CD5678",
        "location": "Swargate, Pune",
        "priority_score": 74,
        "priority_level": "ELEVATED",
        "cases": ["FIR-104", "FIR-087"],
        "details": {
            "age": 29,
            "priors": 2,
            "gang": "Swargate Ring Associate",
            "occupation": "Logistics Driver"
        }
    },
    {
        "id": "ENT-003",
        "name": "MH12AB1234",
        "type": "VEHICLE",
        "model": "Maruti Suzuki Swift (White)",
        "owner": "Rahul Sharma",
        "priority_score": 81,
        "priority_level": "HIGH",
        "cases": ["FIR-104", "FIR-087"],
        "details": {
            "reg_rto": "Pune RTO",
            "engine_no": "K12M-883921",
            "anpr_sightings": 5
        }
    },
    {
        "id": "ENT-004",
        "name": "+91 98765 43210",
        "type": "PHONE",
        "subscriber": "Rahul Sharma",
        "imei": "864209041234567",
        "cases": ["FIR-104"],
        "details": {
            "tower_sector": "Kothrud Central",
            "calls_count": 48
        }
    },
    {
        "id": "ENT-005",
        "name": "+91 98230 11223",
        "type": "PHONE",
        "subscriber": "Amit Verma",
        "imei": "867890123456789",
        "cases": ["FIR-104", "FIR-087"],
        "details": {
            "tower_sector": "Swargate Bus Depot",
            "calls_count": 36
        }
    },
    {
        "id": "ENT-006",
        "name": "TXN-203",
        "type": "TRANSACTION",
        "amount": 75000,
        "currency": "INR",
        "date": "2026-08-13 14:22:00",
        "sender": "Rahul Sharma",
        "receiver": "Amit Verma",
        "cases": ["FIR-104"],
        "details": {
            "mode": "IMPS / Mobile Transfer",
            "bank": "HDFC Bank Pune Branch",
            "remark": "Auto Parts Settlement"
        }
    },
    {
        "id": "ENT-007",
        "name": "Kothrud Tech Park Parking",
        "type": "LOCATION",
        "address": "Paud Road, Kothrud, Pune",
        "lat": 18.5074,
        "lon": 73.8077,
        "cases": ["FIR-104"],
        "details": {
            "cctv_available": True,
            "jurisdiction": "Kothrud PS"
        }
    },
    {
        "id": "ENT-008",
        "name": "Swargate Logistics Hub",
        "type": "LOCATION",
        "address": "Satara Road, Swargate, Pune",
        "lat": 18.5018,
        "lon": 73.8636,
        "cases": ["FIR-087"],
        "details": {
            "cctv_available": True,
            "jurisdiction": "Swargate PS"
        }
    }
]

DEMO_DUPLICATES = [
    {
        "candidate_id": "DUP-101",
        "record_a": {
            "source": "FIR-104",
            "raw_name": "Rahul Sharma",
            "phone": "+91 98765 43210",
            "vehicle": "MH12AB1234",
            "location": "Kothrud, Pune"
        },
        "record_b": {
            "source": "CDR-202",
            "raw_name": "Rahul Sharm",
            "phone": "+91 98765 43210",
            "vehicle": "Not Recorded",
            "location": "Kothrud Sector 2"
        },
        "record_c": {
            "source": "VEH-019",
            "raw_name": "Rahul S.",
            "phone": "+91 98765 43210",
            "vehicle": "MH12AB1234",
            "location": "Pune RTO"
        },
        "match_score": 97,
        "match_reasons": [
            "Phonetic & Levenshtein Name Similarity (94%)",
            "Exact Phone Number Match (+91 98765 43210)",
            "Common Vehicle Link (MH12AB1234)",
            "Geographic Proximity (Kothrud, Pune)"
        ],
        "unified_target_id": "ENT-001",
        "status": "PENDING"
    }
]

DEMO_TIMELINE = [
    {
        "date": "10 Aug 2026",
        "time": "23:45 IST",
        "title": "Getaway Vehicle Sighted on CCTV",
        "description": "White Maruti Swift MH12AB1234 recorded exiting Swargate warehouse perimeter at high speed.",
        "case_id": "FIR-087",
        "evidence": "VEH-019 / CCTV-SWG-04",
        "badge": "VEHICLE SIGHTING",
        "type": "vehicle"
    },
    {
        "date": "11 Aug 2026",
        "time": "18:30 IST",
        "title": "Unusual Spike in CDR Communications",
        "description": "14 encrypted voice calls logged between Rahul Sharma (+91 98765 43210) and Amit Verma (+91 98230 11223) within 48 hours.",
        "case_id": "FIR-104",
        "evidence": "CDR-202",
        "badge": "CDR COMMUNICATION",
        "type": "cdr"
    },
    {
        "date": "12 Aug 2026",
        "time": "09:15 IST",
        "title": "FIR-104 Registered at Kothrud PS",
        "description": "Commercial electronics theft formally lodged. Investigation assigned to Crime Branch Unit 2.",
        "case_id": "FIR-104",
        "evidence": "FIR-104",
        "badge": "FIR LODGED",
        "type": "fir"
    },
    {
        "date": "13 Aug 2026",
        "time": "14:22 IST",
        "title": "High-Value Transaction Executed",
        "description": "Instant IMPS fund transfer of ₹75,000 sent from Rahul Sharma to Amit Verma tagged 'Auto Parts Settlement'.",
        "case_id": "FIR-104",
        "evidence": "FIN-203",
        "badge": "FINANCIAL TRANSACTION",
        "type": "finance"
    }
]

DEMO_CROSS_CASE_INSIGHTS = [
    {
        "insight_id": "INS-001",
        "type": "CROSS-CASE CONNECTION",
        "severity": "CRITICAL",
        "title": "Shared Vehicle MH12AB1234 Links Separate FIRs",
        "summary": "Vehicle MH12AB1234 (White Maruti Swift) registered to Rahul Sharma appears as primary getaway transport in Case FIR-087 (Swargate) and vehicle involved in Case FIR-104 (Kothrud).",
        "cases_involved": ["FIR-104", "FIR-087"],
        "entities_involved": ["Rahul Sharma", "MH12AB1234", "Amit Verma"],
        "evidence_sources": ["FIR-104", "FIR-087", "VEH-019"],
        "confidence": "HIGH (98%)"
    },
    {
        "insight_id": "INS-002",
        "type": "UNUSUAL COMMUNICATION PATTERN",
        "severity": "HIGH",
        "title": "14 Telecommunication Interactions Within 48 Hours",
        "summary": "High-frequency call exchange between suspect Rahul Sharma and logistics driver Amit Verma coinciding with the execution of Case FIR-104.",
        "cases_involved": ["FIR-104"],
        "entities_involved": ["Rahul Sharma", "Amit Verma", "+91 98765 43210", "+91 98230 11223"],
        "evidence_sources": ["CDR-202"],
        "confidence": "VERIFIED (100%)"
    },
    {
        "insight_id": "INS-003",
        "type": "FINANCIAL TRANSFER CORRELATION",
        "severity": "HIGH",
        "title": "₹75,000 Payout Following Incident Occurrence",
        "summary": "Transfer TXN-203 executed 26 hours post-incident from Rahul Sharma to Amit Verma, indicating possible illicit goods settlement.",
        "cases_involved": ["FIR-104"],
        "entities_involved": ["Rahul Sharma", "Amit Verma", "TXN-203"],
        "evidence_sources": ["FIN-203"],
        "confidence": "HIGH (92%)"
    }
]

DEMO_PRIORITY_LEADS = [
    {
        "rank": 1,
        "name": "Rahul Sharma",
        "type": "Person",
        "score": 87,
        "level": "HIGH PRIORITY",
        "breakdown": {
            "network_connectivity": {"score": 30, "max": 35},
            "cross_case_links": {"score": 25, "max": 25},
            "transaction_pattern": {"score": 18, "max": 20},
            "evidence_strength": {"score": 14, "max": 20}
        },
        "reasons": [
            "Cross-case association across FIR-104 and FIR-087",
            "High network degree centrality (6 direct links)",
            "72-hour temporal convergence with theft execution",
            "Immediate ₹75,000 financial transfer to accomplice"
        ],
        "evidence": ["FIR-104", "CDR-202", "FIN-203", "VEH-019"]
    },
    {
        "rank": 2,
        "name": "MH12AB1234",
        "type": "Vehicle",
        "score": 81,
        "level": "HIGH PRIORITY",
        "breakdown": {
            "network_connectivity": {"score": 26, "max": 35},
            "cross_case_links": {"score": 25, "max": 25},
            "transaction_pattern": {"score": 15, "max": 20},
            "evidence_strength": {"score": 15, "max": 20}
        },
        "reasons": [
            "Common physical link connecting FIR-104 (Kothrud) and FIR-087 (Swargate)",
            "ANPR detection at toll plaza near crime scenes",
            "Registered ownership tied to prime suspect"
        ],
        "evidence": ["VEH-019", "FIR-104", "FIR-087"]
    },
    {
        "rank": 3,
        "name": "Amit Verma",
        "type": "Person",
        "score": 74,
        "level": "ELEVATED",
        "breakdown": {
            "network_connectivity": {"score": 24, "max": 35},
            "cross_case_links": {"score": 20, "max": 25},
            "transaction_pattern": {"score": 18, "max": 20},
            "evidence_strength": {"score": 12, "max": 20}
        },
        "reasons": [
            "14 recorded CDR interactions with primary suspect",
            "Recipient of ₹75,000 post-incident payout",
            "Physical co-presence at Swargate logistics hub"
        ],
        "evidence": ["CDR-202", "FIN-203"]
    }
]

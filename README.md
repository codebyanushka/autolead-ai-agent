# AutoLead AI — Autonomous Lead Generation Agent

> An AI-powered browser agent that autonomously searches businesses, navigates websites, and extracts contact information — turning hours of manual prospecting into seconds.

---

## The Problem

Sales and outreach teams spend **3–5 hours daily** manually searching for leads — Googling businesses, opening websites one by one, hunting for contact emails. It's repetitive, slow, and doesn't scale.

## The Solution

AutoLead AI is a fully autonomous LLM-powered agent that does this end-to-end:

1. Takes a natural language query (e.g. *"AI startups in Bangalore"*)
2. Searches the web for matching businesses
3. Navigates each business website autonomously
4. Extracts contact emails and decision-maker info
5. Outputs a structured lead list — ready for outreach

---

## Architecture

```
User Query (natural language)
        ↓
LLM Query Planner — breaks query into search terms
        ↓
Browser Automation Agent
  ├── Web Search → Top N business results
  ├── Website Navigator → Crawls each site
  └── Email Extractor → Finds contact info
        ↓
TypeScript Config Layer — pipeline management + structured output parsing
        ↓
Structured Output → leads list (name, website, email, source)
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent Core | Python |
| LLM | LLM Agents + Prompt Engineering |
| Automation | Browser Automation |
| Pipeline Config | TypeScript |
| Output | Structured JSON / CSV |
| Containerization | Docker |

---

## Features

- **Natural language input** — describe your target market in plain English
- **Autonomous navigation** — agent visits websites without human input
- **Intelligent email extraction** — finds contact pages, about pages, footer emails
- **Scalable pipeline** — TypeScript config layer for managing multiple runs
- **Structured output** — clean JSON/CSV ready for CRM import

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker (optional)

### Installation

```bash
# Clone the repo
git clone https://github.com/codebyanushka/Autolead-ai-agent.git
cd Autolead-ai-agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

### Run

```bash
python src/main.py --query "fintech startups in Mumbai"
```

---

## Environment Variables

```env
LLM_API_KEY=your_key_here
BROWSER_HEADLESS=true
MAX_RESULTS=20
OUTPUT_FORMAT=json
```

---

## Example Output

```json
[
  {
    "company": "Example Corp",
    "website": "https://example.com",
    "email": "contact@example.com",
    "source": "Contact page"
  }
]
```

---

## Future Roadmap

- [ ] Automated outreach email generation (LLM-powered)
- [ ] Lead scoring based on company size + relevance
- [ ] CRM integrations (HubSpot, Notion, Sheets)
- [ ] Dashboard for managing and tracking leads
- [ ] Multi-threaded parallel crawling for 10x speed

---

## Use Cases

- **Sales teams** — build prospect lists in minutes
- **Recruiters** — find hiring managers at target companies
- **Founders** — research competitors and potential partners
- **Marketers** — identify businesses for B2B campaigns

---

## Author

**Anushka Tiwari** — Full-Stack Developer & AI Engineer

[GitHub](https://github.com/codebyanushka) · [LinkedIn](https://linkedin.com/in/anushkaatiwarii)

---

*Built to eliminate repetitive manual work using autonomous AI agents.*

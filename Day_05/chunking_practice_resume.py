

#chunking practice with my resume

def document_chunking(text,chunk_size=200,overlap=20):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap
    return chunks


document = """PRAVEEN TIRUMANI 
Data Analyst  |  Excel  |  SQL  |  Power BI  |  Healthcare & Operations Analytics 
praveen07ml@gmail.com  |  +91 95 4230 3789  |  Hyderabad, India  |  linkedin.com/in/pvntirumani  |  Portfolio 
CAREER OBJECTIVE 
Aspiring Data Analyst with hands-on experience in Excel-based MIS reporting, SQL data management, and Power BI dashboard design. 
Seeking a challenging role in a data-driven organisation where I can apply my analytical skills, Python-based automation, and business 
intelligence capabilities to deliver actionable insights and support informed decision-making. 
TECHNICAL SKILLS 
Data Analysis & Reporting: Excel (Pivot Tables, Charts, Conditional Formatting), Power BI, SQL, MIS Reporting 
Python: Pandas, NumPy (Data Cleaning), API Calling 
Data Management: MySQL, Power Query, Data Extraction, Data Governance, Reconciliation 
Business Intelligence: Power BI, DAX, Dashboard Design, KPI Reporting, Interactive Slicers 
Cloud & Productivity: Microsoft 365, SharePoint, OneDrive, Teams 
Tools & Version Control: Git, GitHub, Jupyter Notebook 
PROJECTS 
Healthcare Appointment No-Show Analysis  |  Excel Analytics  |  GitHub 
Tools: Microsoft Excel  |  Pivot Tables, Charts, Conditional Formatting, KPI Cards, Dashboard Design 
Mar 2025 – May 2025 
• Analysed hospital appointment data to identify no-show patterns across 20,000+ records, segmenting by demographics, departments, 
scheduling behaviour, and medical conditions. 
• Built Excel dashboard with KPI cards and pivot charts; identified overall no-show rate of >20% with departmental and neighbourhood
level breakdowns, enabling targeted intervention strategies. 
• Quantified SMS reminder effectiveness — reminder recipients showed significantly higher attendance — and delivered scheduling 
recommendations for high-risk groups and high no-show weekdays. 
ER Operational Efficiency & Bottleneck Analysis  |  Excel Analytics  |  GitHub 
Tools: Microsoft Excel  |  Power Query, Pivot Tables, Pivot Charts, Conditional Formatting Heatmaps, Interactive Slicers 
Mar 2025 – May 2025 
• Analysed 5,000 simulated ER patient visits to identify peak demand, staffing bottlenecks, and wait time drivers; identified Monday
Tuesday as highest-volume days and doctor-stage as the primary bottleneck. 
• Quantified satisfaction impact: long-wait patients scored 1.8/5 vs 4.6/5 for short-wait categories — providing a measurable case for 
workflow optimisation and peak-hour staffing increases. 
CRM Data Quality & Reconciliation Framework  |  SQL · Python · Power BI  |  GitHub 
Tools: MySQL, Python, Microsoft Excel, Power BI 
Dec 2025 
• Developed structured SQL databases for 15,000+ records, performing data cleansing and cross-source reconciliation using Python 
(Pandas) and SQL, maintaining 95%+ data accuracy. 
• Built Excel reconciliation frameworks and standardised Power BI templates to present findings to non-technical stakeholders, with full 
governance controls and audit-ready outputs. 
EDUCATION 
BV Raju PG College, Bhimavaram 
Andhra Pradesh, India 
Master of Computer Applications (MCA) 
Sri YN College, Narsapur 
Bachelor of Science – Statistics  |  GPA: 9.22 / 10 
CERTIFICATIONS 
Andhra Pradesh, India 
• Shiksha — Data Analyst Certificate — Coursework covering data analytics, SQL, Excel, and business intelligence. 
KEY ACHIEVEMENTS 
• Reduced manual reporting effort by 50% through Excel macro and Python automation across data extraction and consolidation 
workflows. 
• Maintained 95%+ data accuracy through structured validation, reconciliation, and governance controls across multiple projects. 
• Delivered Power BI dashboards and MIS reports for datasets of 15,000–20,000+ records, supporting stakeholder decision-making. 
LANGUAGES 
English: Fluent     
Telugu: Native  """.strip()

chunks = document_chunking(document)


for i,chunk in enumerate(chunks):

    print(f"\nchunk {i+1} -  {chunk}")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from PIL import Image
import io
import numpy as np

# Page configuration
st.set_page_config(
	page_title="Academic Publishing Guide",
	page_icon="📚",
	layout="wide",
	initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #2563EB;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .topic-header {
        font-size: 1.4rem;
        color: #3B82F6;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .highlight {
        background-color: #DBEAFE;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .warning {
        background-color: #FEF2F2;
        color: #B91C1C;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .success {
        background-color: #ECFDF5;
        color: #065F46;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .footnote {
        font-size: 0.8rem;
        color: #6B7280;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Create sidebar navigation
st.sidebar.title("Navigation")
pages = [
	"Introduction to Academic Publishing",
	"Types of Publications",
	"Types of Journals",
	"Understanding Journal Metrics",
	"Access Models: Open Access & Subscriptions",
	"The Publication Process",
	"Writing Your Research Paper",
	"Submission & Peer Review",
	"Predatory Journals: Warning Signs",
	"Publishing Ethics",
	"After Publication: Promotion & Impact"
]
selected_page = st.sidebar.radio("Go to", pages)

# Introduction to the app
st.sidebar.markdown("---")
st.sidebar.info(
	"This interactive guide is designed to help beginners understand the fundamentals "
	"of international academic publishing. Navigate through the different sections "
	"using the menu above."
)


# Helper function to create downloadable PDF
def get_binary_file_downloader_html(bin_data, file_label='File', button_label='Download'):
	bin_str = base64.b64encode(bin_data).decode()
	href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}.pdf"><button style="color: white; background-color: #4CAF50; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;">{button_label}</button></a>'
	return href


# Helper function to create infographics
def create_impact_factor_chart():
	# Sample data for impact factors
	journals = ['Nature', 'Science', 'Cell', 'PNAS', 'NEJM', 'Field-specific Journal']
	impact_factors = [49.962, 47.728, 41.582, 11.205, 91.245, 5.5]
	colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#ff7f0e']

	fig, ax = plt.subplots(figsize=(10, 6))
	bars = ax.bar(journals, impact_factors, color=colors)
	ax.set_title('Example Impact Factors of Top Journals vs. Field-Specific Journals')
	ax.set_ylabel('Impact Factor (2023)')
	ax.set_ylim(0, 100)

	for bar in bars:
		height = bar.get_height()
		ax.annotate(f'{height:.1f}',
					xy=(bar.get_x() + bar.get_width() / 2, height),
					xytext=(0, 3),
					textcoords="offset points",
					ha='center', va='bottom')

	plt.xticks(rotation=45, ha='right')
	plt.tight_layout()

	return fig


def create_publication_timeline():
	# Sample data for publication timeline
	stages = ['Research', 'Writing', 'Journal Selection', 'Submission', 'Initial Review',
			  'Peer Review', 'Revisions', 'Acceptance', 'Publication']
	time_weeks = [0, 12, 13, 14, 16, 24, 32, 36, 48]

	fig, ax = plt.subplots(figsize=(12, 6))
	ax.plot(time_weeks, range(len(stages)), 'bo-', markersize=10)

	for i, stage in enumerate(stages):
		ax.annotate(stage, (time_weeks[i], i), xytext=(10, 0),
					textcoords='offset points', va='center')

	ax.set_yticks([])
	ax.set_xlabel('Weeks (approximate)')
	ax.set_title('Typical Timeline of Academic Publication Process')
	ax.grid(axis='x', linestyle='--', alpha=0.7)

	plt.tight_layout()
	return fig


def create_open_access_chart():
	labels = ['Gold OA', 'Green OA', 'Hybrid', 'Diamond OA', 'Traditional']
	sizes = [30, 25, 20, 10, 15]
	colors = ['#f9d923', '#36AE7C', '#187498', '#4361EE', '#888888']
	explode = (0.1, 0, 0, 0.1, 0)

	fig, ax = plt.subplots(figsize=(10, 7))
	ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
		   shadow=True, startangle=140)
	ax.set_title('Publication Models in Academic Publishing')
	ax.axis('equal')

	plt.tight_layout()
	return fig


# Page content based on selection
if selected_page == "Introduction to Academic Publishing":
	st.markdown("<h1 class='main-header'>Introduction to Academic Publishing</h1>", unsafe_allow_html=True)

	st.markdown("""
    Academic publishing is the process through which researchers share their findings with the broader scientific community 
    and the public. It's a critical part of the research cycle that allows for the verification, critique, 
    and building upon of knowledge.
    """)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown("""
    **Why is academic publishing important?**
    - Disseminates new knowledge and discoveries
    - Establishes intellectual priority and ownership of ideas
    - Provides a record of scholarly achievements
    - Creates a platform for scientific debate and improvement
    - Helps in career advancement and recognition
    - Influences policy decisions and practical applications
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>The Publishing Landscape</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)
	with col1:
		st.markdown("""
        The academic publishing landscape has evolved significantly over the past decades:

        - **Traditional journals**: Established publications with subscription models
        - **Open access movement**: Making research freely available to all
        - **Digital publishing**: Enabling faster dissemination and new formats
        - **Preprint servers**: Allowing early sharing before formal publication
        - **Alternative metrics**: Measuring impact beyond citation counts
        """)

	with col2:
		fig = create_open_access_chart()
		st.pyplot(fig)
		st.caption("Distribution of publication models in academic publishing")

	st.markdown("<h3 class='topic-header'>Key Challenges for Beginners</h3>", unsafe_allow_html=True)
	st.markdown("""
    As a beginner in academic publishing, you'll face several challenges:

    1. **Finding the right journal** for your research
    2. **Understanding publication ethics** and avoiding pitfalls
    3. **Navigating peer review** and responding to feedback
    4. **Writing effectively** for academic audiences
    5. **Avoiding predatory publishers** that may harm your reputation
    6. **Learning publication terminology** and procedures

    This guide will help you navigate these challenges and provide a solid foundation for your publishing journey.
    """)

	st.success(
		"This interactive guide will walk you through each aspect of academic publishing, from understanding different types of publications to successfully publishing in reputable journals.")

elif selected_page == "Types of Publications":
	st.markdown("<h1 class='main-header'>Types of Academic Publications</h1>", unsafe_allow_html=True)

	st.markdown("""
    Academic research can be published in various formats, each serving different purposes and audiences. 
    Understanding these formats will help you choose the most appropriate outlet for your work.
    """)

	publication_types = {
		"Original Research Articles": {
			"description": "Present new, unpublished research, including methodology, results, and discussions",
			"typical_length": "4,000-8,000 words",
			"review_process": "Full peer review",
			"example": "Smith et al. (2023) 'Novel approaches to quantum computing in environmental science', Nature",
			"suitable_for": "Completed research projects with substantial findings"
		},
		"Review Articles": {
			"description": "Synthesize and analyze existing research on a specific topic",
			"typical_length": "6,000-10,000 words",
			"review_process": "Full peer review",
			"example": "Johnson & Garcia (2022) 'A decade of progress in CRISPR gene editing: A comprehensive review', Annual Review of Genetics",
			"suitable_for": "Researchers with broad knowledge of a field wanting to provide an overview"
		},
		"Short Communications/Letters": {
			"description": "Brief reports of significant, novel findings that warrant rapid publication",
			"typical_length": "1,500-3,000 words",
			"review_process": "Expedited peer review",
			"example": "Chen et al. (2024) 'Rapid detection of viral mutations using AI algorithms', Science",
			"suitable_for": "Time-sensitive findings or preliminary results of high importance"
		},
		"Case Studies/Reports": {
			"description": "Detailed analysis of specific instances, patients, or phenomena",
			"typical_length": "2,000-4,000 words",
			"review_process": "Peer review",
			"example": "Patel & Williams (2023) 'Management of rare neurological disorder: A case study', The Lancet Neurology",
			"suitable_for": "Clinical observations, unique cases, or specific implementations"
		},
		"Methodological Papers": {
			"description": "Present new experimental or computational methods, tests, or procedures",
			"typical_length": "3,000-6,000 words",
			"review_process": "Peer review with technical focus",
			"example": "Martinez et al. (2024) 'A novel approach for single-cell RNA sequencing in limited samples', Nature Methods",
			"suitable_for": "Researchers who have developed innovative techniques or improvements"
		},
		"Book Chapters": {
			"description": "Contributions to edited volumes focusing on specific aspects of a broader topic",
			"typical_length": "5,000-10,000 words",
			"review_process": "Editor review, sometimes peer review",
			"example": "Wilson (2023) 'Climate change impacts on urban infrastructure' in 'Climate Adaptation in Cities'",
			"suitable_for": "Established researchers invited to contribute specialized knowledge"
		},
		"Conference Papers/Proceedings": {
			"description": "Research presented at academic conferences, published in proceedings",
			"typical_length": "2,000-5,000 words",
			"review_process": "Varies (abstract review to full peer review)",
			"example": "Rodriguez & Kim (2024) 'Machine learning for predicting protein structures', Proceedings of the 10th AI Conference",
			"suitable_for": "Work in progress or completed research to be presented to peers"
		},
		"Commentaries/Perspectives": {
			"description": "Expert opinions or insights on current issues, trends, or published research",
			"typical_length": "1,000-3,000 words",
			"review_process": "Editorial review",
			"example": "Taylor (2023) 'The future of renewable energy policy', Energy Policy",
			"suitable_for": "Experienced researchers offering context or opinion on important topics"
		},
		"Preprints": {
			"description": "Preliminary versions of research papers shared before formal peer review",
			"typical_length": "Varies by field",
			"review_process": "No formal peer review",
			"example": "Li et al. (2024) 'Preliminary evidence for exoplanet atmospheric composition', arXiv",
			"suitable_for": "Researchers seeking early feedback or establishing priority"
		}
	}

	# Create an interactive element to explore publication types
	selected_pub_type = st.selectbox("Select a publication type to learn more:", list(publication_types.keys()))

	# Display the details of the selected publication type
	pub_details = publication_types[selected_pub_type]

	st.markdown(f"<h3 class='topic-header'>{selected_pub_type}</h3>", unsafe_allow_html=True)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown(f"**Description:** {pub_details['description']}")
	st.markdown(f"**Typical Length:** {pub_details['typical_length']}")
	st.markdown(f"**Review Process:** {pub_details['review_process']}")
	st.markdown(f"**Example:** {pub_details['example']}")
	st.markdown(f"**Best For:** {pub_details['suitable_for']}")
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Choosing the Right Publication Type</h3>", unsafe_allow_html=True)
	st.markdown("""
    Consider these factors when deciding which publication type is best for your research:

    1. **Stage of research**: Completed study or preliminary findings?
    2. **Scope and impact**: Breakthrough finding or incremental advancement?
    3. **Timeliness**: Is rapid publication critical?
    4. **Target audience**: Specialists in your subfield or broader scientific community?
    5. **Career goals**: How will this publication contribute to your research profile?
    """)

	st.info(
		"**Pro Tip:** Many researchers develop a publication strategy that includes different types of publications from a single research project. For example, presenting preliminary findings at a conference, sharing methodological innovations in a specialized journal, and publishing comprehensive results in a high-impact journal.")

elif selected_page == "Types of Journals":
	st.markdown("<h1 class='main-header'>Types of Academic Journals</h1>", unsafe_allow_html=True)

	st.markdown("""
    Academic journals vary widely in scope, prestige, audience, and publishing models. Understanding these differences 
    is crucial for selecting the right venue for your research.
    """)

	st.markdown("<h3 class='topic-header'>Classification by Scope</h3>", unsafe_allow_html=True)

	scope_col1, scope_col2 = st.columns(2)

	with scope_col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Multidisciplinary Journals**
        - Publish research from multiple fields
        - Examples: Nature, Science, PNAS, PLOS ONE
        - Generally higher visibility but more competitive
        - Seek research with broad implications
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Field-Specific Journals**
        - Focus on a particular academic discipline
        - Examples: Cell, Journal of Finance, Physical Review
        - Reach targeted audience in your field
        - Content spans the entire discipline
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with scope_col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Specialized Journals**
        - Concentrate on a specific sub-discipline
        - Examples: Biomacromolecules, Urban Climate, Child Neuropsychology
        - Highly focused readership
        - Deeper technical content appropriate for specialists
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Regional Journals**
        - Focus on research relevant to specific geographic regions
        - Examples: European Journal of Public Health, Latin American Research Review
        - Important for locally-relevant research
        - May have language options beyond English
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Classification by Prestige and Impact</h3>", unsafe_allow_html=True)

	# Visualize impact factors
	st.pyplot(create_impact_factor_chart())
	st.caption("Example impact factors for selected journals (2023 data)")

	tier_col1, tier_col2 = st.columns(2)

	with tier_col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Top-Tier ("Flagship") Journals**
        - Highest impact factors and prestige
        - Very selective (acceptance rates often <10%)
        - Examples: Nature, Science, Cell, NEJM, The Lancet
        - Significant visibility and career impact
        - Long and demanding review process
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Mid-Tier Journals**
        - Respectable impact factors
        - Moderate selectivity (acceptance rates 20-40%)
        - Solid reputation in the field
        - Good visibility to relevant audiences
        - Examples: PLOS ONE, Scientific Reports, field-specific journals
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with tier_col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Specialized High-Impact Journals**
        - High impact within a specific sub-discipline
        - Selective within their niche
        - Examples: Nature Nanotechnology, Psychological Bulletin
        - Excellent visibility to targeted audience
        - Strong reputation among specialists
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Emerging and New Journals**
        - Recently established, building reputation
        - May have innovative publishing models
        - Often open access with faster review times
        - Lower barriers to entry but less established prestige
        - Example: Nature Communications (established 2010)
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Journal Series and Families</h3>", unsafe_allow_html=True)

	st.markdown("""
    Many publishers have developed "families" of journals with different levels of selectivity and scope:

    **Example: Nature Portfolio**
    - Nature (flagship, multidisciplinary)
    - Nature subject journals (Nature Chemistry, Nature Neuroscience, etc.)
    - Nature Communications (less selective but still prestigious)
    - Scientific Reports (even less selective, but still peer-reviewed)

    This tiered system allows for "cascading" peer review, where papers rejected from higher-tier journals 
    may be offered transfer to a more specialized or less selective journal in the same family.
    """)

	st.markdown("<h3 class='topic-header'>Journal Selection Strategy</h3>", unsafe_allow_html=True)

	st.markdown("""
    When selecting a journal, consider:

    1. **Fit with scope**: Does your research match the journal's focus?
    2. **Target audience**: Who needs to see your research?
    3. **Impact vs. acceptance rate**: Balance prestige with publication probability
    4. **Open access requirements**: Funding mandates and visibility needs
    5. **Publication speed**: How quickly do you need to publish?
    6. **Author fees**: Can you afford any associated costs?
    7. **Journal metrics**: Impact factor, CiteScore, etc.
    """)

	st.info(
		"**Pro Tip:** Review recent issues of potential target journals to assess whether your paper's style, methodology, and scope are a good match. Many experienced researchers identify 3-5 potential journals ranked in order of preference before submission.")

elif selected_page == "Understanding Journal Metrics":
	st.markdown("<h1 class='main-header'>Understanding Journal Metrics</h1>", unsafe_allow_html=True)

	st.markdown("""
    Journal metrics are quantitative measures used to assess the relative importance and influence of academic journals. 
    These metrics help researchers evaluate where to publish and help institutions assess research quality.
    """)

	st.markdown("<h3 class='topic-header'>Common Journal Metrics</h3>", unsafe_allow_html=True)

	metrics = {
		"Impact Factor (IF)": {
			"description": "Average number of citations received per paper published in that journal during the two preceding years",
			"publisher": "Clarivate Analytics (Web of Science)",
			"strengths": "Widely recognized, long-established, simple to understand",
			"limitations": "Can be manipulated, field-dependent, affected by outliers, short citation window",
			"example": "Nature (2023): 49.962, NEJM (2023): 91.245"
		},
		"CiteScore": {
			"description": "Similar to Impact Factor but counts citations over 4 years instead of 2",
			"publisher": "Elsevier (Scopus)",
			"strengths": "Larger citation window reduces annual fluctuations, covers more journals than IF",
			"limitations": "Still field-dependent, can be influenced by self-citation practices",
			"example": "Nature (2023): 45.3, Lancet (2023): 63.2"
		},
		"SCImago Journal Rank (SJR)": {
			"description": "Measures weighted citations based on the prestige of the citing journal",
			"publisher": "SCImago Lab (Scopus data)",
			"strengths": "Considers citation quality not just quantity, mitigates field differences",
			"limitations": "More complex to calculate and understand, less widely used",
			"example": "Cell (2023): 13.48, JAMA (2023): 8.56"
		},
		"Source Normalized Impact per Paper (SNIP)": {
			"description": "Measures contextual citation impact by weighting citations based on the total number of citations in a subject field",
			"publisher": "CWTS (Leiden University)",
			"strengths": "Normalizes for differences in citation practices between fields",
			"limitations": "Complex methodology, less intuitive than simple ratios",
			"example": "Science (2023): 7.52, Nature Materials (2023): 6.48"
		},
		"h-index for journals": {
			"description": "A journal has an h-index of h if h of its papers have been cited at least h times",
			"publisher": "Various",
			"strengths": "Captures both productivity and citation impact, resistant to outliers",
			"limitations": "Size-dependent, favors older journals, cumulative measure that always increases",
			"example": "Nature (cumulative): 1120, Science (cumulative): 1089"
		},
		"Eigenfactor": {
			"description": "Rates the total importance of a journal based on citations with a 5-year window, similar to Google's PageRank algorithm",
			"publisher": "University of Washington",
			"strengths": "Eliminates self-citations, accounts for prestige of citing journals, normalizes for field",
			"limitations": "Complex algorithm less transparent to users",
			"example": "Nature (2023): 1.56, Cell (2023): 0.67"
		},
		"Acceptance Rate": {
			"description": "Percentage of submitted manuscripts that are accepted for publication",
			"publisher": "Journals themselves (not always disclosed)",
			"strengths": "Direct measure of selectivity and competition",
			"limitations": "Not standardized, not consistently reported, affected by submission volume",
			"example": "Science: ~7%, PLOS ONE: ~50%"
		}
	}

	# Create interactive element to explore metrics
	selected_metric = st.selectbox("Select a metric to learn more:", list(metrics.keys()))

	# Display information for the selected metric
	metric_details = metrics[selected_metric]

	st.markdown(f"<h3 class='topic-header'>{selected_metric}</h3>", unsafe_allow_html=True)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown(f"**Description:** {metric_details['description']}")
	st.markdown(f"**Published by:** {metric_details['publisher']}")
	st.markdown(f"**Strengths:** {metric_details['strengths']}")
	st.markdown(f"**Limitations:** {metric_details['limitations']}")
	st.markdown(f"**Examples:** {metric_details['example']}")
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Journal Quartiles</h3>", unsafe_allow_html=True)

	st.markdown("""
    Journals are often categorized into quartiles (Q1, Q2, Q3, Q4) based on their metrics within their field:

    - **Q1**: Top 25% of journals in the field
    - **Q2**: Between top 25% and top 50%
    - **Q3**: Between top 50% and top 75%
    - **Q4**: Bottom 25% of journals in the field

    This quartile ranking helps compare journals across different fields, as raw metrics like Impact Factor
    vary significantly between disciplines.
    """)

	# Create a simple visualization of journal quartiles
	quartile_data = pd.DataFrame({
		'Quartile': ['Q1', 'Q2', 'Q3', 'Q4'],
		'Percentile Range': ['75-100', '50-75', '25-50', '0-25'],
		'Typical Characteristics': [
			'Highest visibility and prestige, very selective',
			'Good reputation, moderate selectivity',
			'Emerging or specialized journals',
			'New journals or less established venues'
		]
	})

	st.dataframe(quartile_data, hide_index=True)

	st.markdown("<h3 class='topic-header'>Using Journal Metrics Wisely</h3>", unsafe_allow_html=True)

	st.markdown("""
    Journal metrics should be used thoughtfully:

    1. **Consider multiple metrics**: No single metric tells the complete story
    2. **Compare within fields**: Metrics vary dramatically between disciplines
    3. **Balance with other factors**: Audience, open access options, and review speed matter too
    4. **Beware of manipulation**: Some journals employ tactics to artificially inflate metrics
    5. **Remember the content**: The quality and fit of your paper is more important than chasing metrics
    """)

	st.warning("""
    **Important Note:**
    While journal metrics can guide publication decisions, they're imperfect proxies for quality. Many organizations, 
    including DORA (San Francisco Declaration on Research Assessment), advocate for reducing reliance on journal-based 
    metrics in favor of assessing research on its own merits.
    """)

elif selected_page == "Access Models: Open Access & Subscriptions":
	st.markdown("<h1 class='main-header'>Access Models: Open Access & Subscriptions</h1>", unsafe_allow_html=True)

	st.markdown("""
    The way research is accessed and who pays for publication costs varies significantly across academic publishing. 
    Understanding these access models is crucial for making informed decisions about where to publish.
    """)

	# Visual representation of access models
	fig = create_open_access_chart()
	st.pyplot(fig)
	st.caption("Distribution of publication access models in academic publishing")

	st.markdown("<h3 class='topic-header'>Traditional Subscription Model</h3>", unsafe_allow_html=True)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown("""
    **How it works:**
    - Readers (or their institutions) pay subscription fees to access content
    - Authors typically don't pay to publish
    - Access is restricted to subscribers
    - Also called "closed access" or "paywalled" content

    **Examples:** Most established journals before 2000, many prestigious journals like Science, Nature (main journal), 
    and many society journals

    **Pros:**
    - No publication costs for authors
    - Established prestige and recognition
    - Revenue supports editorial quality and peer review

    **Cons:**
    - Limited readership and visibility
    - Research inaccessible to many potential readers
    - Perpetuates inequalities in access to knowledge
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Open Access Models</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Gold Open Access**

        **How it works:**
        - Content freely available to all readers
        - Authors (or their funders/institutions) pay an Article Processing Charge (APC)
        - Immediate access upon publication

        **Examples:** PLOS journals, BMC series, Scientific Reports

        **Pros:**
        - Maximum visibility and accessibility
        - Higher citation potential
        - Complies with most funder mandates

        **Cons:**
        - APCs can be expensive ($1,500-$5,000+)
        - May create barriers for unfunded researchers
        - Quality concerns with some newer OA journals
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Green Open Access**

        **How it works:**
        - Published in subscription journals but self-archived in repositories
        - Author deposits manuscript in institutional or subject repository
        - May involve embargo period before public access

        **Examples:** arXiv, bioRxiv, institutional repositories

        **Pros:**
        - No direct cost to authors
        - Can publish in prestigious subscription journals
        - Increases accessibility while maintaining traditional publishing

        **Cons:**
        - Often subject to embargo periods (6-24 months)
        - Usually can only share accepted manuscript, not final version
        - Repository versions may lack final formatting
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Hybrid Open Access**

        **How it works:**
        - Subscription journals that offer open access option for individual articles
        - Authors can pay APC to make their specific article open access
        - Other articles remain behind paywall

        **Examples:** Most major publishers offer hybrid options across their portfolio

        **Pros:**
        - Combines prestige of established journals with OA benefits
        - Immediate accessibility upon publication
        - Complies with funder mandates

        **Cons:**
        - Often highest APCs ($3,000-$5,000+)
        - Criticized as "double dipping" (subscription + APC revenue)
        - Complicated licensing and copyright arrangements
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Diamond/Platinum Open Access**

        **How it works:**
        - Free to publish, free to read
        - Costs covered by institutions, societies, or foundations
        - No charges to either authors or readers

        **Examples:** Many society journals, university-supported journals

        **Pros:**
        - Most equitable model for all parties
        - No financial barriers to publishing or reading
        - Often community-governed

        **Cons:**
        - Sustainable funding can be challenging
        - Limited in number compared to other models
        - May have fewer resources for marketing/promotion
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>APC Waivers and Discounts</h3>", unsafe_allow_html=True)

	st.markdown("""
    Many open access publishers offer APC waivers or reductions for:

    - Researchers from low and middle-income countries
    - Early career researchers
    - Researchers without institutional or grant funding
    - Institutional membership arrangements

    **Always check publisher websites for waiver policies before assuming you cannot afford to publish open access.**
    """)

	st.markdown("<h3 class='topic-header'>Transformative Agreements</h3>", unsafe_allow_html=True)

	st.markdown("""
    A growing trend is "transformative agreements" between publishers and institutions/consortia:

    - Combines subscription access with open access publishing rights
    - Institutions pay a single fee covering both reading access and OA publishing for their researchers
    - Aims to transition from subscription to open access publishing
    - Examples include "Read and Publish" and "Publish and Read" agreements

    **Check with your library or research office to see if your institution has such agreements that cover your APC costs.**
    """)

	st.markdown("<h3 class='topic-header'>Making Your Decision</h3>", unsafe_allow_html=True)

	st.markdown("""
    When deciding on an access model for your publication:

    1. **Check funder requirements**: Many require open access publication
    2. **Consider your target audience**: Who needs to access your research?
    3. **Evaluate available funding**: Do you have funds for APCs?
    4. **Review institutional agreements**: Your institution may cover costs
    5. **Assess career implications**: Balance prestige and accessibility
    6. **Explore green OA options**: Secondary archiving can expand access
    """)

	st.info("""
    **Pro Tip:** The "Journal Checker Tool" (https://journalcheckertool.org/) helps researchers identify journals 
    that comply with specific funder open access policies, taking into account institutional agreements.
    """)

elif selected_page == "The Publication Process":
	st.markdown("<h1 class='main-header'>The Publication Process: From Idea to Publication</h1>",
				unsafe_allow_html=True)

	st.markdown("""
    The journey from research idea to published paper involves multiple steps and stakeholders. Understanding this process 
    helps set realistic expectations and navigate the system effectively.
    """)

	# Display timeline chart
	st.pyplot(create_publication_timeline())
	st.caption("Approximate timeline of the academic publication process (varies by field and journal)")

	st.markdown("<h3 class='topic-header'>Stage 1: Pre-Submission</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Research and Analysis**
    - Conduct research following rigorous methods
    - Analyze data and draw conclusions
    - Discuss findings with colleagues and get feedback

    **Writing the Manuscript**
    - Follow standard structure (IMRaD: Introduction, Methods, Results, and Discussion)
    - Create clear figures and tables
    - Draft a compelling abstract and introduction
    - Ensure proper citation of relevant literature

    **Journal Selection**
    - Identify journals that match your research scope
    - Evaluate journal metrics, audience, and access models
    - Review author guidelines for formatting requirements
    - Consider publication timelines and acceptance rates

    **Pre-Submission Peer Review**
    - Share with colleagues for informal review
    - Address feedback before submission
    - Consider using preprint servers for early feedback
    """)

	st.markdown("<h3 class='topic-header'>Stage 2: Submission and Initial Review</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Manuscript Submission**
    - Create account in journal's submission system
    - Prepare cover letter highlighting significance
    - Format manuscript according to journal guidelines
    - Submit required forms (conflicts of interest, author contributions, etc.)

    **Initial Editorial Screen**
    - Editor reviews for scope and basic quality
    - Decision to send to peer review or reject (desk rejection)
    - This stage typically takes 1-2 weeks

    **Common Reasons for Desk Rejection:**
    - Out of scope for the journal
    - Insufficient novelty or significance
    - Major methodological flaws
    - Poor writing or presentation
    - Incomplete submission materials
    """)

	st.markdown("<h3 class='topic-header'>Stage 3: Peer Review</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("""
        **Reviewer Selection**
        - Editor identifies appropriate reviewers (2-4 typically)
        - Reviewers accept or decline invitation
        - Finding willing reviewers can take several weeks

        **Review Process**
        - Reviewers evaluate:
          - Methodology and technical soundness
          - Significance and novelty
          - Data quality and analysis
          - Literature contextualization
          - Clarity and presentation
        - Review period: 2-8 weeks depending on journal
        """)

	with col2:
		st.markdown("""
        **Types of Peer Review**

        - **Single-blind**: Reviewers know authors' identities, but authors don't know reviewers'
        - **Double-blind**: Neither party knows the other's identity
        - **Open peer review**: Identities known to both parties, reviews may be published
        - **Transparent review**: Reviews published alongside the article
        - **Collaborative review**: Reviewers discuss with each other
        - **Post-publication review**: Public commentary after publication
        """)

	st.markdown("<h3 class='topic-header'>Stage 4: Editorial Decision</h3>", unsafe_allow_html=True)

	st.markdown("""
    Based on peer reviews, editors make one of several decisions:

    **Accept (rare for first submission)**
    - Paper accepted as is, minimal changes needed
    - Typically occurs only after revision rounds

    **Minor Revision**
    - Paper requires small changes
    - Likely to be accepted if addressed adequately
    - May not require full re-review

    **Major Revision**
    - Substantial changes needed
    - May require additional experiments or analyses
    - Will undergo re-review after revision

    **Reject and Resubmit**
    - Paper has merit but needs extensive reworking
    - Treated as new submission after changes

    **Reject**
    - Paper not suitable for the journal
    - May recommend submission to another journal
    """)

	st.markdown("<h3 class='topic-header'>Stage 5: Revision and Resubmission</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Addressing Reviewer Comments**
    - Carefully address each reviewer point
    - Prepare detailed response letter explaining changes
    - Make manuscript changes with track changes/highlighting
    - Add new data or analyses if required

    **Resubmission**
    - Submit revised manuscript with response letter
    - Include cover letter summarizing major changes

    **Re-Review**
    - Original reviewers evaluate revisions
    - May involve fewer reviewers or editor-only review for minor revisions
    - This process may iterate multiple times
    """)

	st.markdown("<h3 class='topic-header'>Stage 6: Acceptance and Production</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Acceptance**
    - Formal acceptance notification
    - Copyright transfer or licensing agreement
    - Payment of any applicable fees (APCs)

    **Production Process**
    - Copyediting for grammar and style
    - Typesetting and layout
    - Figure preparation and formatting
    - Author review of proofs
    - Correction of any errors in proofs

    **Publication**
    - Online publication (typically precedes print)
    - Assignment of DOI (Digital Object Identifier)
    - Inclusion in issue (for traditional journals)
    """)

	st.markdown("<h3 class='topic-header'>Stage 7: Post-Publication</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Promotion**
    - Share via social media and academic networks
    - Deposit in repositories (if allowed)
    - Present at conferences

    **Tracking Impact**
    - Monitor citations and altmetrics
    - Address any post-publication comments
    - Consider related follow-up publications

    **Corrections or Retractions (if necessary)**
    - Submit corrections for minor errors
    - Address any serious concerns transparently
    """)

	st.success("""
    **Success Factors for Publication:**

    - **Rigorous research**: Strong methodology and analysis
    - **Clear writing**: Well-structured, concise presentation
    - **Significance**: Clear explanation of importance and novelty
    - **Responsiveness**: Constructive engagement with peer review
    - **Persistence**: Willingness to revise and possibly resubmit elsewhere if rejected
    """)

elif selected_page == "Writing Your Research Paper":
	st.markdown("<h1 class='main-header'>Writing Your Research Paper</h1>", unsafe_allow_html=True)

	st.markdown("""
    Writing an effective research paper requires both scientific rigor and clear communication. 
    This guide will help you structure your manuscript and avoid common pitfalls.
    """)

	st.markdown("<h3 class='topic-header'>Standard Paper Structure (IMRaD)</h3>", unsafe_allow_html=True)

	paper_sections = {
		"Title": {
			"purpose": "Concisely describe the paper's content and attract readers",
			"tips": "Be specific, include key concepts, avoid jargon, keep under 15 words if possible",
			"example": "CRISPR-Cas9 Gene Editing Reverses Antibiotic Resistance in Pathogenic E. coli Strains",
			"common_mistakes": "Too vague, too technical, too long, or using unnecessary words like 'A study of...'"
		},
		"Abstract": {
			"purpose": "Summarize the entire paper in a single paragraph",
			"tips": "Include background, objective, methods, results, and conclusion in 150-300 words",
			"example": "Antibiotic resistance poses a global health threat. Here we demonstrate that CRISPR-Cas9 gene editing can effectively reverse resistance to ampicillin in E. coli strains by targeting the beta-lactamase gene. We developed a modified delivery system using bacteriophage vectors that achieved 87% editing efficiency in vitro and 64% in mouse models. Treated bacterial populations showed renewed susceptibility to ampicillin treatment with MIC values comparable to non-resistant strains. These results demonstrate a potential strategy for combating antibiotic resistance in clinical settings.",
			"common_mistakes": "Including too much detail, omitting key results, using undefined abbreviations, exceeding word limits"
		},
		"Introduction": {
			"purpose": "Provide context, establish importance, and state research questions",
			"tips": "Move from broad field to specific gap, clearly state objectives at the end",
			"example": "Starting with the global problem of antibiotic resistance, narrowing to beta-lactam resistance mechanisms, identifying the specific gap in reversing established resistance, then stating the specific objective to use CRISPR-Cas9 to target resistance genes",
			"common_mistakes": "Too long/short, failing to justify importance, unclear research question, excessive literature review"
		},
		"Methods": {
			"purpose": "Describe how the research was conducted with enough detail for replication",
			"tips": "Use subheadings, provide specific details of materials, procedures, and analyses",
			"example": "Detailed sections on bacterial strain selection, CRISPR-Cas9 construct design, bacteriophage vector preparation, transfection protocols, and statistical analysis approaches",
			"common_mistakes": "Insufficient detail for replication, excessive detail on standard procedures, poor organization, omitting statistical methods"
		},
		"Results": {
			"purpose": "Present findings without interpretation",
			"tips": "Use clear figures and tables, highlight key findings, organize logically",
			"example": "Presenting editing efficiency data, antibiotic susceptibility testing results, and in vivo efficacy findings with appropriate statistical analyses and clear figures",
			"common_mistakes": "Interpreting results (save for discussion), presenting raw data without analysis, poor figure design, redundant presentation"
		},
		"Discussion": {
			"purpose": "Interpret results, place in context, address limitations, and suggest implications",
			"tips": "Begin with key findings summary, compare with existing literature, acknowledge limitations, suggest applications",
			"example": "Interpreting the significance of achieved editing efficiency, comparing with other approaches to combat resistance, discussing delivery challenges, addressing potential for resistance to the CRISPR system itself, and suggesting clinical applications",
			"common_mistakes": "Simply repeating results, overinterpreting findings, ignoring limitations, making claims beyond the data"
		},
		"Conclusion": {
			"purpose": "Summarize key findings and their importance",
			"tips": "Brief, impactful, focuses on contribution to the field",
			"example": "This work demonstrates that CRISPR-Cas9 gene editing can effectively reverse established antibiotic resistance in pathogenic bacteria, offering a potential new approach to address this critical public health challenge.",
			"common_mistakes": "Introducing new information, being too vague, merely repeating the abstract"
		},
		"References": {
			"purpose": "Acknowledge sources and provide evidence",
			"tips": "Follow journal-specific format exactly, ensure all citations are included",
			"example": "Comprehensive list of relevant literature formatted according to journal requirements (e.g., APA, Vancouver, Harvard styles)",
			"common_mistakes": "Formatting inconsistencies, missing citations, excessive self-citation, outdated sources"
		}
	}

	# Create interactive element to explore paper sections
	selected_section = st.selectbox("Select a paper section to learn more:", list(paper_sections.keys()))

	# Display the details of the selected section
	section_details = paper_sections[selected_section]

	st.markdown(f"<h3 class='topic-header'>{selected_section}</h3>", unsafe_allow_html=True)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown(f"**Purpose:** {section_details['purpose']}")
	st.markdown(f"**Tips:** {section_details['tips']}")
	st.markdown(f"**Example:** {section_details['example']}")
	st.markdown(f"**Common Mistakes:** {section_details['common_mistakes']}")
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Writing Style for Academic Papers</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Clarity and Precision**
        - Use precise, specific language
        - Define all technical terms and abbreviations
        - One idea per paragraph with clear topic sentences
        - Use simple sentence structures for complex ideas
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Objectivity**
        - Use passive voice judiciously (not exclusively)
        - Avoid emotional or subjective language
        - Support claims with evidence
        - Distinguish between facts and interpretations
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Conciseness**
        - Eliminate unnecessary words and redundancies
        - Use specific nouns rather than vague descriptions
        - Choose direct verbs ("shows" instead of "is showing")
        - Break up long sentences into shorter ones
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Flow and Cohesion**
        - Use transition words between ideas
        - Create logical progression between paragraphs
        - Link sentences with connecting words
        - Maintain consistent terminology throughout
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Tables and Figures</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Effective Figures**
    - Should be self-explanatory with comprehensive captions
    - Use high resolution (300+ dpi) for publication
    - Consider colorblind-friendly color schemes
    - Simplify and focus on key data (avoid "chart junk")
    - Label axes clearly with units

    **Effective Tables**
    - Use for precise numerical data that's hard to visualize
    - Include clear column and row headings
    - Use footnotes for explanations and abbreviations
    - Align numbers appropriately (decimals aligned)
    - Don't duplicate information in text and tables

    **Figure and Table Placement**
    - Reference every figure and table in the text
    - Place near relevant text discussion
    - Number consecutively throughout the paper
    - Follow journal guidelines for placement
    """)

	st.markdown("<h3 class='topic-header'>Ethical Considerations in Writing</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Authorship**
    - Include all who made substantial contributions
    - Determine order according to field conventions and contribution
    - Get explicit agreement from all authors before submission
    - Provide specific author contributions in many journals

    **Plagiarism and Self-Plagiarism**
    - Always cite sources for ideas, methods, and data
    - Rewrite in your own words rather than paraphrasing closely
    - Don't reuse substantial portions of your previous publications without citation
    - Use plagiarism detection software before submission

    **Data Presentation**
    - Present data completely and honestly
    - Don't selectively report only favorable results
    - Explain any data exclusions with justification
    - Maintain raw data for potential verification
    """)

	st.markdown("<h3 class='topic-header'>Practical Writing Tips</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Before Writing**
    - Create a detailed outline
    - Identify target journal and review its requirements
    - Organize your figures and tables
    - Review similar papers in your target journal

    **During Writing**
    - Write the Methods and Results sections first
    - Leave the Introduction and Discussion for later
    - Write the Abstract last
    - Use reference management software (Zotero, Mendeley, EndNote)

    **After Writing**
    - Let the manuscript "rest" before editing
    - Read aloud to catch awkward phrasing
    - Have colleagues review for clarity and content
    - Check journal-specific formatting requirements
    - Verify all references are accurate and formatted correctly
    """)

	st.info("""
    **Pro Tip:** Write regularly in shorter sessions rather than in marathon sessions. Research shows that consistent writing 
    (e.g., 1-2 hours daily) is more productive than occasional long sessions.
    """)

elif selected_page == "Submission & Peer Review":
	st.markdown("<h1 class='main-header'>Submission & Peer Review Process</h1>", unsafe_allow_html=True)

	st.markdown("""
    The submission and peer review process is critical to academic publishing. Understanding how it works 
    will help you navigate this phase successfully and respond effectively to reviewer feedback.
    """)

	st.markdown("<h3 class='topic-header'>Preparing for Submission</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Final Manuscript Checklist**
        - All authors have approved final version
        - Manuscript follows journal formatting guidelines
        - Figures and tables are high quality and properly labeled
        - References are complete and correctly formatted
        - Word count, abstract length meet requirements
        - Supplementary materials are prepared if needed
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Required Submission Documents**
        - Cover letter
        - Main manuscript file
        - Figures (often as separate files)
        - Tables (may be in manuscript or separate)
        - Supplementary materials
        - Disclosure forms (conflicts of interest, etc.)
        - Author contribution statements
        - Data availability statements
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Writing an Effective Cover Letter</h3>", unsafe_allow_html=True)

	st.markdown("""
    A well-crafted cover letter can influence editors' initial impression of your manuscript.
    """)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown("""
    **Cover Letter Components**

    1. **Journal information**: Editor's name, journal name, date
    2. **Manuscript information**: Title, article type, word count
    3. **Introduction paragraph**: Brief statement about your submission
    4. **Significance paragraph**: Why your work matters and fits this journal
    5. **Novelty statement**: What's new about your research
    6. **Confirmation statements**:
       - Not under consideration elsewhere
       - All authors approve submission
       - Any conflicts of interest
    7. **Suggested reviewers**: Names and contacts of potential reviewers (if requested)
    8. **Closing**: Polite conclusion and contact information
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("""
    **Cover Letter Example:**

    ```
    April 27, 2025

    Dr. Sarah Johnson
    Editor-in-Chief
    Journal of Environmental Microbiology

    Dear Dr. Johnson,

    I am pleased to submit our manuscript entitled "Microbial Community Dynamics in Arctic Permafrost Under Climate Change Conditions" for consideration as a Research Article in the Journal of Environmental Microbiology.

    This study addresses the critical knowledge gap regarding how microbial communities in permafrost respond to thawing conditions. Using a combination of metagenomic sequencing and functional gene analysis, we have documented previously unrecognized shifts in microbial populations that accelerate carbon release during permafrost thaw. Our findings demonstrate that certain microbial taxa serve as early indicators of ecosystem transition, potentially providing a new monitoring approach for climate change impacts in Arctic regions.

    Our work is novel in its use of in situ sampling coupled with controlled laboratory simulations, allowing us to bridge the gap between field observations and mechanistic understanding. The results have significant implications for climate models that currently underestimate microbial contributions to carbon cycling in thawing permafrost.

    This manuscript has not been published or submitted for publication elsewhere. All authors have approved this submission and have no conflicts of interest to disclose. Data from this study has been deposited in the ENA database (accession number PRJEB000000).

    We suggest the following experts as potential reviewers:
    - Dr. Michael Chen, University of Alaska (mchen@alaska.edu), expert in permafrost microbiology
    - Dr. Elena Rodriguez, Norwegian Polar Institute (rodriguez.e@npi.no), specialist in Arctic microbial ecology

    Thank you for considering our manuscript. I am the corresponding author and can be reached at your.email@university.edu or +1-555-123-4567.

    Sincerely,

    Your Name
    Associate Professor
    Department of Environmental Sciences
    University of Research
    ```
    """)

	st.markdown("<h3 class='topic-header'>The Peer Review Process</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Typical Workflow**

    1. **Submission**: You submit manuscript through journal's online system
    2. **Editorial screening**: Editor checks if paper meets basic requirements and fits scope
    3. **Reviewer assignment**: Editor invites appropriate reviewers (usually 2-3)
    4. **Review period**: Reviewers evaluate manuscript (typically 2-8 weeks)
    5. **Decision compilation**: Editor considers reviews and makes initial decision
    6. **Author notification**: You receive decision and reviewer comments
    7. **Revision process**: You address reviewer comments (if not rejected)
    8. **Resubmission**: You submit revised manuscript with detailed response
    9. **Re-evaluation**: Editor/reviewers assess revisions
    10. **Final decision**: Accept, further revisions, or reject
    """)

	st.markdown("<h3 class='topic-header'>Types of Peer Review</h3>", unsafe_allow_html=True)

	peer_review_types = {
		"Single-blind": {
			"description": "Reviewers know authors' identities, but authors don't know reviewers",
			"advantages": "Reviewers can assess based on authors' previous work and reputation",
			"disadvantages": "Potential bias based on author's institution, nationality, or reputation",
			"common in": "Many traditional journals across disciplines"
		},
		"Double-blind": {
			"description": "Neither reviewers nor authors know each other's identities",
			"advantages": "Reduces potential bias based on author characteristics",
			"disadvantages": "Authors can sometimes be identified by self-citations or specific methods",
			"common in": "Social sciences, humanities, some medical journals"
		},
		"Open peer review": {
			"description": "Reviewer and author identities are disclosed to each other",
			"advantages": "Transparency, accountability, potential for more constructive feedback",
			"disadvantages": "Junior reviewers may be hesitant to criticize senior authors",
			"common in": "BMJ, BioMed Central journals, growing trend in scientific publishing"
		},
		"Transparent peer review": {
			"description": "Review reports are published alongside the article (with or without reviewer names)",
			"advantages": "Shows the development of the paper, allows evaluation of review quality",
			"disadvantages": "May make reviewers more cautious in their critiques",
			"common in": "Nature Communications, EMBO journals, PeerJ"
		},
		"Collaborative peer review": {
			"description": "Reviewers interact with each other, sometimes with authors, during the review process",
			"advantages": "Allows discussion and consensus-building among reviewers",
			"disadvantages": "More time-consuming, potential for dominant personalities to influence",
			"common in": "eLife, F1000Research"
		},
		"Post-publication peer review": {
			"description": "Articles are published first, then openly reviewed and discussed",
			"advantages": "Rapid publication, community involvement in evaluation",
			"disadvantages": "Potential damage if significant flaws discovered after publication",
			"common in": "F1000Research, ScienceOpen, PubPeer comments"
		}
	}

	# Create interactive element to explore peer review types
	selected_review_type = st.selectbox("Select a peer review type to learn more:", list(peer_review_types.keys()))

	# Display the details of the selected peer review type
	review_type_details = peer_review_types[selected_review_type]

	st.markdown(f"<h4>{selected_review_type}</h4>", unsafe_allow_html=True)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown(f"**Description:** {review_type_details['description']}")
	st.markdown(f"**Advantages:** {review_type_details['advantages']}")
	st.markdown(f"**Disadvantages:** {review_type_details['disadvantages']}")
	st.markdown(f"**Common in:** {review_type_details['common in']}")
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Understanding Editorial Decisions</h3>", unsafe_allow_html=True)

	decisions = {
		"Accept": "Paper is accepted as is or with minimal copyediting changes. Very rare for first submissions.",
		"Minor Revisions": "Paper is provisionally accepted pending small changes. Typically doesn't require full re-review.",
		"Major Revisions": "Substantial changes needed but editors see potential. Will require thorough re-review.",
		"Reject and Resubmit": "Current version rejected but a substantially revised version would be considered as a new submission.",
		"Reject": "Paper is not suitable for the journal. May be due to quality issues or lack of fit with journal scope."
	}

	for decision, description in decisions.items():
		st.markdown(f"**{decision}**: {description}")

	st.markdown("<h3 class='topic-header'>Responding to Reviewer Comments</h3>", unsafe_allow_html=True)

	st.markdown("""
    The response to reviewers is a critical document that can determine whether your revised manuscript is accepted. 
    A well-structured response demonstrates professionalism and thoroughness.
    """)

	st.markdown("<div class='highlight'>", unsafe_allow_html=True)
	st.markdown("""
    **Effective Response Strategy**

    1. **Be comprehensive**: Address every single comment
    2. **Be respectful**: Maintain a polite, professional tone even with harsh reviews
    3. **Be clear**: Use a structured format that makes it easy to follow your responses
    4. **Be specific**: Indicate exactly what changes you made and where
    5. **Be strategic**: Make all reasonable changes, but respectfully defend when necessary

    **Suggested Response Format**

    ```
    Response to Reviewers

    We thank the reviewers for their thoughtful comments that have helped improve our manuscript. Below we address each point in detail.

    Reviewer #1:

    Comment 1: "The sample size seems inadequate for the statistical analyses performed."
    Response: We agree with the reviewer that our sample size requires careful consideration. We have:
    1) Added power analysis justifying our sample size (page 5, paragraph 2)
    2) Applied more appropriate statistical tests for small sample sizes (Methods, page 8)
    3) Acknowledged this limitation in the Discussion (page 15)

    Comment 2: [continue with each comment]

    Reviewer #2:
    [same format]
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Dealing with Rejection</h3>", unsafe_allow_html=True)

	st.markdown("""
    Rejection is a normal part of academic publishing that even established researchers experience regularly.

    **When Your Paper is Rejected:**

    1. **Take time to process**: Allow yourself a cooling-off period before responding
    2. **Evaluate reviews objectively**: Look for constructive feedback even in harsh reviews
    3. **Decide on next steps**:
       - Revise and submit to another journal
       - Consider a journal cascade system (some publishers offer automatic referral)
       - Substantially revise and resubmit if "reject and resubmit" is offered
       - Appeal the decision (only in cases of demonstrable reviewer error)
    4. **Learn from the experience**: Use feedback to improve future submissions

    **When Resubmitting to a Different Journal:**
    - Update the format to match new journal requirements
    - Revise based on previous reviewer comments
    - Consider mentioning previous review in your cover letter (if major improvements were made)
    - Choose an appropriate journal based on feedback about scope or significance
    """)

	st.success("""
    **Pro Tip:** Many successful papers were rejected from their first-choice journals. A study of high-impact papers 
    found that approximately 75% had been rejected at least once before finding the right home.
    """)

elif selected_page == "Predatory Journals: Warning Signs":
	st.markdown("<h1 class='main-header'>Predatory Journals: Warning Signs</h1>", unsafe_allow_html=True)

	st.markdown("""
    Predatory journals exploit the academic publishing model by charging publication fees without providing legitimate 
    peer review, editorial services, or proper indexing. Identifying and avoiding these journals is essential for 
    protecting your research and reputation.
    """)

	st.warning("""
    **Important:** Publishing in predatory journals can damage your academic reputation, waste research funds, 
    and prevent your work from reaching its intended audience. These publications may appear legitimate at first glance, 
    so careful evaluation is necessary.
    """)

	st.markdown("<h3 class='topic-header'>What Are Predatory Journals?</h3>", unsafe_allow_html=True)

	st.markdown("""
    Predatory journals are publications that prioritize profit over scholarly integrity by:

    - Charging article processing fees without providing proper editorial services
    - Falsely claiming to perform peer review
    - Promising rapid publication regardless of quality
    - Misleading authors about their indexing, impact factor, or editorial board
    - Using aggressive email solicitation to recruit submissions

    These journals exploit researchers' need to publish, particularly affecting early-career researchers, 
    those under publication pressure, or researchers from regions with less publishing experience.
    """)

	st.markdown("<h3 class='topic-header'>Red Flags and Warning Signs</h3>", unsafe_allow_html=True)

	warning_categories = [
		"Communication and Solicitation",
		"Website and Presentation",
		"Editorial Board and Peer Review",
		"Publication Metrics and Indexing",
		"Fees and Transparency",
		"Content and Quality"
	]

	warning_signs = {
		"Communication and Solicitation": [
			"Unsolicited emails with effusive praise for your previous work",
			"Promises of rapid peer review (e.g., 'decision in 1 week')",
			"Invitations to submit to journals outside your field of expertise",
			"Poor grammar and spelling in communications",
			"Overly flattering or personal tone in solicitation emails"
		],
		"Website and Presentation": [
			"Poorly designed, unprofessional website with broken links",
			"Spelling and grammatical errors throughout the site",
			"Mixing different scientific fields without clear sections",
			"Missing or vague contact information (e.g., no physical address)",
			"Journal name mimicking a well-established journal",
			"Use of terms like 'International', 'Global', or 'World' to seem legitimate"
		],
		"Editorial Board and Peer Review": [
			"Editorial board members not listed or with no affiliations",
			"Board members listed without their knowledge or permission",
			"No information about the peer review process",
			"Extremely brief peer review timeframes (days rather than weeks)",
			"Single person serving as editor for multiple journals",
			"No expertise in the field evident among editors"
		],
		"Publication Metrics and Indexing": [
			"False claims about impact factor or invented metrics",
			"Claims of indexing in major databases that cannot be verified",
			'Using misleading metrics (e.g., "Journal Impact Factor" instead of official "Impact Factor")',
			"Claiming to be indexed in Google Scholar (which isn't a selective index)",
			"Falsely claiming to be included in Web of Science or Scopus"
		],
		"Fees and Transparency": [
			"Hidden fees revealed only after acceptance",
			"Unclear information about APCs on the website",
			"No clear policies on copyright and licensing",
			"Absence of retraction, correction, or ethics policies",
			"No information about digital preservation"
		],
		"Content and Quality": [
			"Previously published papers with minimal editing",
			"Articles on topics outside the journal's stated scope",
			"Obvious lack of copyediting in published articles",
			"Low-quality figures and tables in published papers",
			"Extremely short or extremely long articles without justification",
			"Papers accepted without revisions despite obvious flaws"
		]
	}

	# Create tabs for different categories of warning signs
	tabs = st.tabs(warning_categories)

	for i, tab in enumerate(tabs):
		category = warning_categories[i]
		with tab:
			st.subheader(category)
			for warning in warning_signs[category]:
				st.markdown(f"🚩 {warning}")

	st.markdown("<h3 class='topic-header'>How to Verify Journal Legitimacy</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Check Established Lists and Directories**

        **Inclusion in these sources is a positive sign:**
        - Directory of Open Access Journals (DOAJ)
        - Journal Citation Reports (Clarivate)
        - Scopus (Elsevier)
        - Major subject-specific indexes in your field

        **Check against these cautionary lists:**
        - Beall's List (archive versions still available)
        - Cabell's Predatory Reports (subscription required)
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Evaluate Publisher Reputation**

        **Reputable publishers typically include:**
        - Major commercial publishers (Elsevier, Springer Nature, Wiley, etc.)
        - Established academic societies and associations
        - University presses
        - Recognized open access publishers (PLOS, Frontiers, MDPI, etc.)

        **Resources to check publishers:**
        - Open Access Scholarly Publishers Association (OASPA) membership
        - Committee on Publication Ethics (COPE) membership
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("""
    **Additional Verification Steps**

    1. **Search for the journal's articles** in major academic databases
    2. **Check editor credentials** by searching for them on institutional websites and publication databases
    3. **Review recently published articles** for quality and relevance
    4. **Verify impact factor claims** directly on Journal Citation Reports
    5. **Ask colleagues and mentors** about their knowledge of the journal
    6. **Use the Think. Check. Submit.** checklist (thinkchecksubmit.org)
    """)

	st.markdown("<h3 class='topic-header'>What If You've Already Submitted?</h3>", unsafe_allow_html=True)

	st.markdown("""
    If you realize you've submitted to a potentially predatory journal:

    1. **Request immediate withdrawal** of your manuscript
    2. **Document all communications** with the journal
    3. **Contact your institution's legal department** if the journal refuses withdrawal
    4. **Be prepared to pay a withdrawal fee** in some cases
    5. **Check if the copyright transfer form** has been signed (complicates withdrawal)
    6. **Report the journal** to relevant authorities and warning lists
    """)

	st.markdown("<h3 class='topic-header'>Hijacked Journals and Conferences</h3>", unsafe_allow_html=True)

	st.markdown("""
    Be aware of these sophisticated predatory tactics:

    **Journal Hijacking**
    - Predators create fake websites mimicking legitimate journals
    - They copy names, ISSNs, and layouts of established journals
    - Only the submission email and payment information differ
    - Always access journals through official publisher platforms or DOI links

    **Fake Conferences**
    - Predatory conferences charge high registration fees with minimal organization
    - They may list prominent speakers without their knowledge
    - Often use vague, multidisciplinary themes to attract wide participation
    - Verify conference legitimacy through professional societies in your field
    """)

	st.success("""
    **Pro Tip:** Use the "PLAN" approach to evaluate journals:
    - **P**resence: Check for physical address, clear contact information, and proper registration
    - **L**egitimacy: Verify indexing claims and editorial board members
    - **A**cademic standards: Review their peer review process and published articles
    - **N**avigation: Evaluate website professionalism and transparency
    """)

elif selected_page == "Publishing Ethics":
	st.markdown("<h1 class='main-header'>Publishing Ethics</h1>", unsafe_allow_html=True)

	st.markdown("""
    Ethical considerations are fundamental to maintaining the integrity of scientific literature. Understanding and 
    adhering to ethical standards is essential for all researchers throughout the publication process.
    """)

	st.markdown("<h3 class='topic-header'>Authorship Ethics</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Who Qualifies as an Author?**

    According to the International Committee of Medical Journal Editors (ICMJE), authorship should be based on the following criteria:

    1. **Substantial contributions** to conception, design, data acquisition, or analysis/interpretation
    2. **Drafting or critically revising** the manuscript for important intellectual content
    3. **Final approval** of the version to be published
    4. **Agreement to be accountable** for all aspects of the work

    All individuals who meet these criteria should be authors; those who don't meet all criteria should be acknowledged instead.
    """)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Authorship Malpractices to Avoid**

        **Ghost authorship:** Omitting contributors who qualify as authors

        **Gift authorship:** Including individuals who did not substantially contribute

        **Guest authorship:** Adding prestigious names who had minimal involvement

        **Coercive authorship:** Supervisors demanding authorship without meeting criteria
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Best Practices for Authorship**

        **Discuss authorship early:** Establish expectations at project start

        **Document contributions:** Keep records of each person's role

        **Follow field conventions:** Author order significance varies by discipline

        **Use CRediT taxonomy:** Consider using Contributor Roles Taxonomy
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Plagiarism and Self-Plagiarism</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Types of Plagiarism**

    **Direct plagiarism:** Copying text verbatim without attribution

    **Mosaic plagiarism:** Combining phrases from multiple sources without proper citation

    **Idea plagiarism:** Using someone's ideas without acknowledgment

    **Self-plagiarism:** Reusing substantial portions of your own previously published work without citation

    **Text recycling:** Reusing portions of your previous writing in a new manuscript
    """)

	st.markdown("""
    **Avoiding Plagiarism**

    1. **Cite all sources** of data, ideas, and language
    2. **Use quotation marks** for direct quotes
    3. **Paraphrase properly** by completely restructuring sentences and using your own vocabulary
    4. **Check your manuscript** with plagiarism detection software before submission
    5. **Cite your own previous work** when building upon it
    """)

	st.markdown("<h3 class='topic-header'>Research Integrity and Data Ethics</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Data Fabrication and Falsification**

        **Fabrication:** Inventing data or results

        **Falsification:** Manipulating research materials, equipment, or processes, or changing/omitting data

        **Image manipulation:** Inappropriate alteration of images that misrepresents findings

        **Cherry-picking:** Selectively reporting only favorable data
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Responsible Data Practices**

        **Data availability:** Share underlying data when possible

        **Transparency about methods:** Provide sufficient detail for replication

        **Declare limitations:** Acknowledge constraints and weaknesses

        **Proper statistical analysis:** Use appropriate tests and avoid p-hacking
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Conflicts of Interest</h3>", unsafe_allow_html=True)

	st.markdown("""
    A conflict of interest exists when professional judgment concerning a primary interest may be influenced by a secondary interest.
    """)

	st.markdown("""
    **Types of Conflicts**

    **Financial conflicts:**
    - Research funding from companies with interest in results
    - Personal investments in related companies
    - Paid consulting for industry related to research area
    - Patents or royalties related to the research

    **Non-financial conflicts:**
    - Personal relationships with editors, reviewers, or competitors
    - Intellectual or academic competition
    - Personal beliefs that might influence interpretation
    - Institutional affiliations affecting objectivity
    """)

	st.markdown("""
    **Managing Conflicts of Interest**

    1. **Disclose all potential conflicts** in your manuscript
    2. **Follow journal-specific disclosure forms** carefully
    3. **Declare funding sources** and their role in the research
    4. **Be transparent about relationships** with commercial entities
    5. **Consider recusing yourself** from certain research roles if conflicts are significant
    """)

	st.markdown("<h3 class='topic-header'>Publication Ethics in Peer Review</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Ethical Issues for Reviewers**

        **Confidentiality:** Not sharing manuscripts under review

        **Competence:** Only reviewing within areas of expertise

        **Conflicts:** Declining reviews when conflicts exist

        **Timeliness:** Completing reviews within agreed timeframe

        **Constructive criticism:** Providing helpful, respectful feedback
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Ethical Issues for Authors**

        **Simultaneous submission:** Not submitting to multiple journals simultaneously

        **Salami slicing:** Inappropriately dividing research into multiple papers

        **Duplicate publication:** Publishing the same content more than once

        **Citation manipulation:** Unnecessarily adding citations to increase metrics

        **Reviewer suggestions:** Not suggesting reviewers with conflicts
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Research Ethics and Participant Protection</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Human Subjects Research**

    1. **Ethics committee approval:** Document IRB/Ethics Committee approval
    2. **Informed consent:** Verify all participants gave proper consent
    3. **Privacy protection:** Ensure anonymity and data security
    4. **Vulnerable populations:** Document special protections when applicable
    5. **Clinical trial registration:** Register trials before participant enrollment

    **Animal Research**

    1. **Ethics committee approval:** Document IACUC approval
    2. **3Rs principle:** Demonstrate replacement, reduction, and refinement
    3. **Humane treatment:** Document proper care and humane endpoints
    4. **Reporting standards:** Follow ARRIVE guidelines
    """)

	st.markdown("<h3 class='topic-header'>Addressing Ethical Breaches</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Post-Publication Issues**

    **Corrections:** Published to address minor errors that don't invalidate results

    **Expressions of concern:** Editors signal potential serious issues under investigation

    **Retractions:** Paper is withdrawn from the scientific record due to serious flaws

    **Reporting concerns:** Anyone can report potential ethical issues to journals
    """)

	st.markdown("""
    **Resources for Publication Ethics**

    - **Committee on Publication Ethics (COPE):** Guidelines and flowcharts
    - **World Association of Medical Editors (WAME):** Resources for ethical standards
    - **Council of Science Editors (CSE):** White papers on publication ethics
    - **Office of Research Integrity (ORI):** Educational resources and case studies
    - **Institution Research Integrity Offices:** Local guidance and support
    """)

	st.info("""
    **Pro Tip:** When facing an ethical dilemma in publishing, consult your institution's research 
    integrity office or ethics committee for guidance. Being proactive about ethics questions is 
    always better than addressing problems after publication.
    """)

elif selected_page == "After Publication: Promotion & Impact":
	st.markdown("<h1 class='main-header'>After Publication: Promotion & Impact</h1>", unsafe_allow_html=True)

	st.markdown("""
    Publication is not the end of the research process—it's the beginning of your work's journey into the scientific 
    community. Actively promoting your research can significantly increase its visibility, readership, citations, 
    and real-world impact.
    """)

	st.markdown("<h3 class='topic-header'>Why Promote Your Research?</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Benefits of Research Promotion**

    1. **Increased readership and citations:** More readers typically leads to more citations
    2. **Enhanced visibility within and beyond your field:** Reach potential collaborators
    3. **Greater research impact:** Influence policy, practice, and future research
    4. **Career advancement:** Build your professional reputation
    5. **Public engagement:** Connect research with society and stakeholders
    6. **Funder requirements:** Meet dissemination obligations
    """)

	st.markdown("<h3 class='topic-header'>Promotion Strategies</h3>", unsafe_allow_html=True)

	promotion_tabs = st.tabs([
		"Academic Channels",
		"Digital Promotion",
		"Media Engagement",
		"Conferences & Events",
		"Institutional Resources"
	])

	with promotion_tabs[0]:
		st.subheader("Academic Channels")

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Academic Social Networks**

        - **ResearchGate & Academia.edu:** Upload papers, track metrics, connect with colleagues
        - **Google Scholar Profile:** Maintain current publication list and track citations
        - **ORCID & Scopus Author ID:** Ensure proper attribution and discoverability
        - **Mendeley & Zotero Groups:** Share in relevant reference groups

        **Best practices:**
        - Keep profiles updated with all publications
        - Add accessible summaries for non-specialists
        - Respond to questions and comments
        - Follow relevant researchers in your field
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Repositories and Preprint Servers**

        - **Institutional repositories:** Archive in your university's system
        - **Subject repositories:** Deposit in field-specific archives (arXiv, bioRxiv, etc.)
        - **Preprint updates:** Link published version to preprints
        - **Zenodo & Figshare:** Share data, code, and supplementary materials

        **Best practices:**
        - Follow journal policies on repository versions
        - Include DOI links to final published version
        - Tag with appropriate keywords for discoverability
        - Include all supplementary materials and data
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with promotion_tabs[1]:
		st.subheader("Digital Promotion")

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Social Media Strategies**

        - **Twitter/X:** Share key findings with relevant hashtags, tag collaborators
        - **LinkedIn:** Post professional updates about publications
        - **Facebook Groups:** Share in relevant academic groups
        - **Instagram & TikTok:** Consider visual summaries for broader audiences

        **Best practices:**
        - Create visually appealing graphics highlighting key findings
        - Use accessible language for broader audience
        - Include link to full paper or open access version
        - Tag co-authors, institutions, and funders
        - Time posts for maximum visibility
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Digital Content Creation**

        - **Blog posts:** Write detailed, accessible summaries
        - **Infographics:** Create visual representations of key findings
        - **Video abstracts:** Record brief explanations of your research
        - **Podcasts:** Discuss your research on relevant shows
        - **Webinars:** Present findings in online seminars

        **Best practices:**
        - Focus on the "so what" factor—why findings matter
        - Use different formats for different audiences
        - Repurpose content across multiple platforms
        - Include clear calls to action (read full paper, contact for collaboration)
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with promotion_tabs[2]:
		st.subheader("Media Engagement")

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Working with Institutional Media Relations**

        - **Press releases:** Work with PR office on announcements
        - **Media training:** Prepare for interviews and public communication
        - **Expert database:** Register as an expert in your field
        - **Pitching stories:** Identify newsworthy aspects of your research

        **Best practices:**
        - Alert PR office well before publication date
        - Prepare lay summaries and talking points
        - Have high-quality images available
        - Be available for interviews after publication
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Direct Media Approaches**

        - **The Conversation:** Write articles for this academic-journalist platform
        - **Journalist connections:** Build relationships with science journalists
        - **Science Media Centers:** Register as an expert source
        - **Reddit AMAs:** Consider "Ask Me Anything" sessions

        **Best practices:**
        - Focus on the broader significance of findings
        - Avoid jargon and explain complex concepts simply
        - Be prepared for challenging questions
        - Respect embargo dates set by journals
        - Maintain scientific accuracy while simplifying
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with promotion_tabs[3]:
		st.subheader("Conferences & Events")

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Conference Presentations**

        - **Oral presentations:** Submit abstracts to relevant conferences
        - **Poster sessions:** Create engaging visual presentations
        - **Specialized workshops:** Present to targeted audiences
        - **Virtual conferences:** Expand reach beyond physical attendance

        **Best practices:**
        - Include QR codes linking to papers on posters
        - Prepare handouts with key findings and contact information
        - Practice presentations for timing and clarity
        - Network actively during the conference
        - Follow up with interested contacts afterward
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Academic and Public Events**

        - **Department seminars:** Present at your institution and others
        - **Public lectures:** Engage with broader community
        - **Science festivals:** Participate in public engagement events
        - **Industry conferences:** Present to potential users of research

        **Best practices:**
        - Adapt presentation style to audience knowledge level
        - Create interactive elements when possible
        - Collect contact information from interested attendees
        - Follow up with specific audiences for potential collaboration
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with promotion_tabs[4]:
		st.subheader("Institutional Resources")

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **University Support Systems**

        - **Research office:** Utilize promotion resources and networks
        - **Library services:** Work with scholarly communications librarians
        - **Alumni networks:** Share through university alumni channels
        - **Department websites:** Ensure research is featured

        **Best practices:**
        - Provide materials for institutional newsletters
        - Contribute to annual research highlights
        - Participate in research showcase events
        - Suggest your work for institutional social media
        """)
		st.markdown("</div>", unsafe_allow_html=True)

		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Funder and Publisher Resources**

        - **Publisher promotion:** Work with journal marketing teams
        - **Funder highlights:** Submit for funder success stories
        - **Publisher platforms:** Utilize journal/publisher social media
        - **Altmetric tracking:** Monitor and amplify high-attention articles

        **Best practices:**
        - Notify funders of publications resulting from their support
        - Share publisher-created promotional materials
        - Tag publishers and funders in social media posts
        - Express interest in being featured in publisher highlights
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Measuring Research Impact</h3>", unsafe_allow_html=True)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Traditional Metrics**

        **Citation counts:** Number of times your paper is cited

        **Journal Impact Factor:** Reflects journal's citation performance

        **h-index:** Measures both productivity and citation impact

        **Field-weighted citation impact:** Normalizes citations by field

        **Tools to track:**
        - Google Scholar
        - Web of Science
        - Scopus
        - Dimensions
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='highlight'>", unsafe_allow_html=True)
		st.markdown("""
        **Alternative Metrics (Altmetrics)**

        **Social media mentions:** Twitter, Facebook, etc.

        **Media coverage:** News articles and broadcasts

        **Policy documents:** Citations in regulations and guidelines

        **Downloads and views:** Reader engagement metrics

        **Tools to track:**
        - Altmetric.com
        - PlumX
        - ImpactStory
        - Journal article pages
        """)
		st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='topic-header'>Long-term Impact Strategies</h3>", unsafe_allow_html=True)

	st.markdown("""
    **Creating Research Narratives**

    1. **Connect related publications:** Reference your previous work appropriately
    2. **Develop research streams:** Build cohesive research programs
    3. **Create research websites:** Dedicated sites for major projects
    4. **Track impact stories:** Document real-world applications and influence

    **Building on Your Publications**

    1. **Follow-up studies:** Address limitations and next questions
    2. **Meta-analyses and reviews:** Synthesize your contribution to the field
    3. **Methodology papers:** Elaborate on novel techniques
    4. **Translation and application:** Move from theory to practice

    **Engagement with Scientific Community**

    1. **Respond to citations:** Engage with those building on your work
    2. **Join relevant discussions:** Participate in scholarly debates
    3. **Offer to collaborate:** Reach out to complementary researchers
    4. **Mentor junior researchers:** Help others build on your findings
    """)

	st.success("""
    **Pro Tip:** Create a promotion plan before publication. The first few weeks after publication are 
    critical for visibility. Having graphics, summaries, and outreach strategies ready in advance will 
    maximize your paper's initial impact.
    """)

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.info(
	"This app was created to help researchers understand the academic publishing process. "
	"Navigate through different topics using the menu above."
)

# Footer
st.markdown("---")
st.markdown(
	"<p class='footnote'>This guide is for educational purposes only. Publishing practices vary by field and journal.</p>",
	unsafe_allow_html=True)
st.markdown("<p class='footnote'>© 2025 Academic Publishing Guide</p>", unsafe_allow_html=True)
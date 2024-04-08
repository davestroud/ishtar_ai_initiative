import streamlit as st
from PIL import Image

# Function to load the image
def load_image(image_file):
    img = Image.open(image_file)
    return img

# Centered title and subheader
centered_title_subheader = """
    <div style='text-align: center'>
        <h1>ISHTAR AI</h1>
        <h2>Utilizing LLMs to support efforts in war torn regions throughout the world</h2>
    </div>
    """
st.markdown(centered_title_subheader, unsafe_allow_html=True)

# Load and display the image
image_path = "app/ishtar_ai.jpeg"
image = load_image(image_path)
st.image(image, caption='ISHTAR AI', use_column_width=True)


# Additional Initiative Text
additional_text = """
This initiative is committed to leveraging the potential of Artificial Intelligence
and Large Language Models to tackle pressing challenges across war-torn regions in 
areas such as Humanitarian Aid and Relief Operations, Monitoring and Analysis of 
Conflict Zones, Cultural and Historical Preservation, Public Health Initiatives, 
Reconstruction Efforts, Peacebuilding and Reconciliation, and Education and Skill 
Development. By utilizing advanced technology, we aim to improve the distribution 
of humanitarian aid, enhance the surveillance of conflict dynamics and displacement 
patterns, safeguard invaluable cultural heritage, bolster public health strategies, 
assist in the rebuilding of critical infrastructure, support peace and reconciliation
endeavors, and provide vital education and training opportunities. Our goal is to 
apply AI-driven approaches to make a meaningful difference, promoting sustainable 
progress, resilience, and harmony in regions ravaged by conflict.

1. **Humanitarian Aid and Relief Operations**
   - Needs Assessment: LLMs can analyze reports, social media, and satellite imagery to identify areas most in need of humanitarian aid, optimizing resource allocation.
   - Logistics Planning: Planning and optimizing the delivery routes and schedules for humanitarian aid to conflict or disaster-affected regions.

2. **Monitoring and Analysis of Conflict Zones**
   - Conflict Tracking: Aggregating and analyzing news reports, social media, and other open-source intelligence to monitor ongoing conflicts and security developments.
   - Displacement Monitoring: Tracking movements of displaced populations to better understand migration patterns and immediate needs for shelters, food, and medical care.

3. **Cultural and Historical Preservation**
   - Documenting Heritage Sites: Utilizing LLMs to aggregate information, images, and research on historical sites for preservation efforts, especially those at risk of destruction due to conflict.
   - Cultural Education: Creating educational content on Syria’s rich cultural history and heritage to promote understanding and preservation.

4. **Public Health Initiatives**
   - Disease Outbreak Analysis: Analyzing data from various sources to predict and monitor disease outbreaks among vulnerable populations, especially in refugee camps.
   - Mental Health Support: Offering AI-driven mental health support services to individuals affected by the conflict, including PTSD support and counseling.

5. **Reconstruction Efforts**
   - Infrastructure Planning: Assisting in the planning and rebuilding of critical infrastructure by analyzing damage assessments, resource needs, and prioritizing projects based on urgency and impact.
   - Economic Development: Analyzing market trends, agricultural data, and economic indicators to support recovery efforts and sustainable development.

6. **Peacebuilding and Reconciliation**
   - Dialogue Facilitation: Supporting peacebuilding efforts by facilitating communication between different factions, including language translation and sentiment analysis to foster understanding.
   - Reconciliation Initiatives: Gathering narratives and experiences from different communities to aid in reconciliation processes and documenting war crimes or human rights abuses for accountability.

7. **Education and Skill Development**
   - Remote Education: Providing remote learning resources and opportunities for displaced children and adults, including language learning, vocational training, and educational content across various subjects.
   - Professional Training for Aid Workers: Developing specialized training modules for aid workers and volunteers on the ground in Syria, including language skills, cultural sensitivity training, and crisis management.

"""
st.markdown(additional_text)

# Expanders for each country
countries = ['Afghanistan', 'Iraq', 'Syria', 'Yemen', 'Somalia', 'Libya']
information = {
    'Afghanistan': """Conflict Overview: Afghanistan's conflict history spans over four decades, beginning with the Soviet invasion in 1979, followed by civil unrest, the emergence of the Taliban in the 1990s, the US-led invasion in 2001, and the eventual return to Taliban control in 2021. The conflict has involved various factions including the Afghan government, the Taliban, US and NATO allies, and numerous insurgent groups, driven by ideological, ethnic, and geopolitical complexities.

Displacement: The enduring conflict has led to significant displacement, creating one of the world's largest populations of refugees and internally displaced persons (IDPs). The UNHCR reports approximately 2.6 million Afghan refugees globally, alongside millions more displaced within Afghanistan itself due to ongoing hostilities and insecurity.

Casualties: Afghanistan has witnessed extensive human suffering, with tens of thousands of civilians killed and countless more injured. The United Nations Assistance Mission in Afghanistan (UNAMA) has documented tens of thousands of civilian casualties since it began its systematic records in 2009, highlighting the conflict's devastating impact on the Afghan population.

Infrastructure Damage: The conflict has extensively damaged Afghanistan's infrastructure, impacting homes, educational institutions, healthcare facilities, and critical public services. This destruction impedes access to essential healthcare and education, further exacerbating the challenges faced by the Afghan people.

Humanitarian Aid Needs: Afghanistan's humanitarian crisis is acute, with widespread food insecurity, lack of clean water, and healthcare access, compounded by the need for basic shelter and essentials. The situation has deteriorated with the COVID-19 pandemic and recent political upheavals, escalating the demand for immediate international humanitarian intervention.

Recovery and Reconstruction Efforts: International organizations, NGOs, and government initiatives have been involved in Afghanistan's recovery and reconstruction efforts, focusing on infrastructure rebuilding, service restoration, economic recovery, and support for displaced populations' return and reintegration. Nonetheless, the efforts are hampered by ongoing political instability, security challenges, and limited financial resources, slowing the country's reconstruction and recovery progress.""",
    'Iraq': """Conflict Overview: Iraq has faced decades of conflict, starting with the Iran-Iraq War in the 1980s, the Gulf War in the early 1990s, the 2003 US-led invasion that toppled Saddam Hussein, and the subsequent insurgency, leading to the rise of the Islamic State (IS) group in 2014. These conflicts have involved a multitude of actors, including Iraqi government forces, US and coalition forces, various insurgent groups, and IS fighters, with the underlying causes ranging from sectarian tensions to geopolitical interests.

Displacement: The cumulative impact of these conflicts has led to significant displacement within Iraq. At the height of the IS crisis, millions were displaced. Although many have returned home, the International Organization for Migration (IOM) reports that there are still hundreds of thousands of internally displaced persons (IDPs) in Iraq, along with Iraqi refugees in neighboring countries.

Casualties: The human toll in Iraq has been enormous, with hundreds of thousands of deaths, including civilians, security forces, and combatants across the different phases of conflict. The violence associated with IS alone resulted in tens of thousands of deaths and injuries, according to the United Nations and various human rights organizations.

Infrastructure Damage: Iraq's infrastructure has suffered extensively due to the conflicts, with significant destruction to homes, schools, hospitals, and critical utilities. The battle against IS, particularly in cities like Mosul, resulted in widespread devastation, rendering large areas uninhabitable and disrupting basic services.

Humanitarian Aid Needs: The needs in Iraq remain substantial, with ongoing requirements for food assistance, medical care, shelter, and support for returning populations. The conflict with IS exacerbated pre-existing vulnerabilities, and despite the end of major combat operations, many communities continue to face challenges in accessing basic necessities.

Recovery and Reconstruction Efforts: Post-IS, Iraq has embarked on extensive recovery and reconstruction efforts, with international support from entities like the United Nations Development Programme (UNDP) and various countries. These efforts focus on rebuilding infrastructure, restoring public services, and supporting economic recovery and social cohesion. However, the scale of destruction and the complexity of Iraq's sectarian and political landscape pose significant challenges to full recovery.""""",
    'Syria': 'Information about Syria...',
    'Yemen': 'Information about Yemen...',
    'Somalia': 'Information about Somalia...',
    'Libya': 'Information about Libya...'
}

for country in countries:
    with st.expander(f"Information about {country}"):
        st.write(information[country])
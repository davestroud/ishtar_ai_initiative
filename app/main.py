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
    'Syria': """Conflict Overview: The Syrian conflict began in 2011 as part of the Arab Spring protests, escalating into a civil war that has drawn in various factions, including the Syrian government, opposition groups, Kurdish forces, and extremist groups like ISIS, as well as international actors through direct intervention or support to proxies. The conflict's origins are rooted in demands for democratic reforms and escalated due to governmental crackdowns, sectarian divisions, and geopolitical interests.

Displacement: The Syrian war has caused one of the largest displacement crises in recent history. According to the United Nations High Commissioner for Refugees (UNHCR), it has generated over 5.6 million Syrian refugees and displaced about 6.7 million people within the country, totaling nearly half of Syria's pre-war population.

Casualties: The toll on human life has been catastrophic, with estimates of civilian deaths varying widely due to the conflict's complexity. Reliable sources estimate hundreds of thousands of deaths, with the Syrian Observatory for Human Rights reporting over 500,000 fatalities, including civilians, government forces, and various combatant groups.

Infrastructure Damage: Syria's infrastructure has been decimated, with widespread destruction to homes, healthcare facilities, schools, and utilities. Key urban centers like Aleppo, Homs, and Raqqa have seen intense battles, leaving significant portions of these cities in ruins and severely disrupting civilian life and access to essential services.

Humanitarian Aid Needs: The humanitarian situation in Syria is dire, with millions requiring assistance for basic needs such as food, water, healthcare, and shelter. The conflict has severely limited access to medical services, and there is an acute need for medical supplies, treatment for injuries, and support for chronic conditions exacerbated by the war.

Recovery and Reconstruction Efforts: While some areas in Syria have seen attempts at recovery and reconstruction, the ongoing conflict, economic collapse, and international sanctions have significantly hampered these efforts. Limited reconstruction has occurred in government-controlled areas, but full-scale rebuilding is contingent on a political solution and substantial international funding, which remains elusive due to the conflict's unresolved nature and geopolitical complexities.""",
    'Yemen': """Conflict Overview: The conflict in Yemen, often described as a proxy war, began in 2014 when the Houthi movement took control of the capital, Sanaa, and much of the northern part of the country, forcing the internationally recognized government to flee to the south, then to Saudi Arabia. A coalition led by Saudi Arabia and the United Arab Emirates intervened in 2015 to restore the government. The conflict involves various factions, including the Houthi rebels, the Yemeni government, southern separatists, and jihadist groups, with regional implications involving Saudi Arabia and Iran.

Displacement: The conflict has resulted in massive displacement within Yemen, with over 4 million internally displaced persons (IDPs) according to the United Nations Office for the Coordination of Humanitarian Affairs (OCHA). Additionally, thousands of Yemenis have sought refuge in neighboring countries.

Casualties: The war has caused tens of thousands of deaths, including a significant number of civilians, due to direct conflict, airstrikes, and other military operations. The Armed Conflict Location & Event Data Project (ACLED) reports extensive casualties, and the actual numbers are likely higher due to underreporting and challenges in data collection.

Infrastructure Damage: Yemen's infrastructure has been severely impacted, with widespread destruction of homes, schools, healthcare facilities, and essential public utilities. This damage exacerbates an already dire humanitarian situation, with many areas lacking access to clean water, electricity, and healthcare services.

Humanitarian Aid Needs: Yemen is considered the world's worst humanitarian crisis, with approximately 80% of the population requiring humanitarian assistance and protection. Needs include food security, medical supplies and services, clean water, sanitation, and shelter. The situation is compounded by economic collapse, a blockade that limits imports, and a locust plague affecting food production.

Recovery and Reconstruction Efforts: Recovery and reconstruction efforts in Yemen face significant challenges due to ongoing conflict, political instability, and a lack of funding. While there are initiatives aimed at providing immediate humanitarian aid, comprehensive reconstruction efforts require a sustained peace process and significant international support to rebuild the country's infrastructure, economy, and social fabric.""",
    'Somalia': """Conflict Overview: The conflict in Somalia has its roots in the collapse of the central government in 1991, leading to decades of civil war, clan conflicts, and the rise of the Islamist militant group Al-Shabaab. The conflict involves the Federal Government of Somalia, supported by African Union Mission in Somalia (AMISOM) troops, against various insurgent groups, primarily Al-Shabaab, which aims to establish an Islamic state in Somalia. The conflict is compounded by territorial disputes, political fragmentation, and foreign intervention.

Displacement: The ongoing violence, combined with natural disasters such as droughts and floods, has led to widespread displacement. According to the United Nations High Commissioner for Refugees (UNHCR), there are over 2.6 million internally displaced persons (IDPs) within Somalia and nearly a million Somali refugees in neighboring countries, making it one of the most significant displacement crises globally.

Casualties: The human cost of the conflict in Somalia has been high, with thousands of civilians killed or injured. Accurate casualty figures are challenging to obtain due to the ongoing nature of the conflict and limited access to many areas. However, it's known that the violence has resulted in significant civilian, militant, and security force casualties over the years.

Infrastructure Damage: Somalia's infrastructure has suffered severely from the prolonged conflict, with extensive damage to homes, schools, healthcare facilities, and basic utilities. Many areas lack access to clean water and electricity, significantly hindering development and humanitarian efforts.

Humanitarian Aid Needs: The humanitarian situation in Somalia is dire, with millions requiring assistance due to the combined effects of conflict, displacement, and climatic shocks. Needs include emergency food aid, medical care, shelter, water, and sanitation services. The situation is exacerbated by periodic outbreaks of diseases such as cholera and measles, particularly in IDP camps.

Recovery and Reconstruction Efforts: Efforts to recover and reconstruct Somalia face numerous challenges, including ongoing security threats, political instability, and funding shortfalls. Initiatives led by the Somali government and supported by international partners focus on rebuilding critical infrastructure, strengthening governance and the rule of law, and promoting economic recovery. However, progress is often slow and uneven across different regions of the country.""",
    'Libya': """Conflict Overview: The Libyan conflict began with the 2011 Arab Spring that led to the overthrow of Muammar Gaddafi. The power vacuum resulted in the country splitting between rival factions: the UN-recognized Government of National Accord (GNA) based in Tripoli and the Libyan National Army (LNA) led by Khalifa Haftar in the east. The conflict has drawn in multiple international actors, with varying degrees of support for each side, complicating the peace process and leading to a protracted civil war characterized by shifting alliances and territorial control.

Displacement: The ongoing conflict has led to significant displacement, with hundreds of thousands of internally displaced persons (IDPs) within Libya. According to the International Organization for Migration (IOM), there are also Libyan refugees who have fled to neighboring countries, seeking safety from the violence.

Casualties: The fighting has resulted in thousands of deaths and injuries among combatants and civilians alike. Precise numbers are challenging to determine due to the ongoing nature of the conflict, but the Human Rights Watch and other organizations have documented significant casualties and human rights abuses on all sides.

Infrastructure Damage: Libya’s infrastructure has sustained considerable damage, with numerous reports of destroyed homes, schools, healthcare facilities, and public utilities. The conflict has severely impacted essential services, including access to healthcare, clean water, and electricity, particularly in areas of intense fighting.

Humanitarian Aid Needs: The conflict, compounded by political instability and economic decline, has left a large portion of the Libyan population in need of humanitarian aid. Critical needs include food, medical care, shelter, and access to clean water and sanitation facilities. The situation is further exacerbated by the COVID-19 pandemic, which has strained the already limited health services.

Recovery and Reconstruction Efforts: Efforts towards recovery and reconstruction in Libya are hindered by the ongoing conflict and lack of a unified national government. Despite several peace talks and ceasefires, sustained recovery efforts require political stability and reconciliation. International organizations and UN agencies are involved in providing humanitarian assistance and supporting ceasefire and election processes, but comprehensive reconstruction of infrastructure and the economy awaits a lasting resolution to the conflict."""
}

for country in countries:
    with st.expander(f"Information about {country}"):
        st.write(information[country])
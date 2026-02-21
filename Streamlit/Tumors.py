import streamlit as st

def app():

    st.set_page_config(layout='wide')

    col1,col2 = st.columns([1.2,1])

    with col1:
        st.markdown("""<h4>-----Select Tumor type-----</h4>""",unsafe_allow_html=True)
        options = st.selectbox("",("","Glioma", "Meningioma", "Pituitary","No Tumor"))

        if options=='Glioma':
            st.image(r"C:\Users\ADMIN\Desktop\glioma.jpg")
        elif options=='Meningioma':
            st.image(r"C:\Users\ADMIN\Desktop\meningioma.jpg")
        elif options=='Pituitary':
            st.image(r'C:\Users\ADMIN\Desktop\pituitary.jpg')

    with col2:
        if options =='Glioma':
            st.write('''
                ** What Is Glioma?

A glioma is a type of tumor that starts in the glial cells of the brain or spinal cord. Glial cells support and protect nerve cells (neurons).
Gliomas are a type of brain tumor and can range from slow-growing to very aggressive
                     
** Types of Glioma
* Common types include:
- Astrocytoma – Starts in astrocytes (star-shaped glial cells).
- Oligodendroglioma – Starts in oligodendrocytes.
- Ependymoma – Starts in ependymal cells lining brain ventricles or spinal cord.
- Glioblastoma – The most aggressive and fast-growing type.
- Doctors also grade gliomas from Grade 1 (slow-growing) to Grade 4 (very aggressive). 
                                       
** Why Does Glioma Happen
* The exact cause is often unknown, but possible risk factors include:
- Genetic mutations (changes in DNA)
- Family history of brain tumors (rare)
- Previous radiation exposure to the head
- Certain genetic disorders
- Most gliomas are not caused by lifestyle and are not usually preventable.    
                                    
** Which Area Does It Affect?
- Gliomas can occur in:
- Brain (most common)
- Spinal cord                   
** Within the brain, they can affect different areas like:
- Frontal lobe (personality, thinking, movement)
- Temporal lobe (memory, speech)
- Parietal lobe (sensation)
- Occipital lobe (vision)
- Brainstem (breathing, vital functions)
- Symptoms depend on the location and size
                     
** Common Symptoms
- Persistent headaches
- Seizures
- Vomiting
- Weakness in arms or legs
- Memory problems
- Personality changes
- Vision or speech problem
                     
** What Needs to Be Done to Treat (or Cure) It?
                     
Treatment depends on the type, grade, size, and location.\n
1️⃣ Surgery
Doctors try to remove as much of the tumor as possible\n
2️⃣ Radiation Therapy
Uses high-energy rays to kill cancer cells\n
3️⃣ Chemotherapy
Medicines to kill tumor cells\n
4️⃣ Targeted Therapy / Clinical Trials
In some cases

** Can Glioma Be Cured?
\nLow-grade gliomas (Grade 1–2): Sometimes controlled for many years, sometimes curable if fully removed.
\nHigh-grade gliomas (Grade 3–4, like glioblastoma): Hard to cure completely, but treatment can prolong life and improve quality of life.
Early diagnosis improves outcomes

\n** Important
If someone has symptoms like frequent headaches, seizures, or neurological changes, they should see a neurologist and get brain imaging (like MRI).
                    ''')

        if options=='Meningioma':
            st.write("""
                ** What Is Meningioma?

A meningioma is a tumor that develops from the meninges — the protective layers covering the brain and spinal cord.
Unlike glioma (which starts inside brain tissue), meningioma grows from the covering around the brain, not from the brain cells themselves.
Most meningiomas are slow-growing and non-cancerous (benign).

** Why Does Meningioma Happen?

** The exact cause is often unknown, but risk factors include:
- Previous radiation exposure to the head
- Hormonal factors (more common in women)
- Genetic conditions like neurofibromatosis type 2
- Age (more common after age 40)
- Many cases happen without a clear cause.

** Which Area Does It Affect?
Meningiomas can grow anywhere the meninges exist, including:
- Brain surface (most common)
- Skull base
- Around the spinal cord
- Common brain areas affected:
- Frontal region (personality, thinking changes)
- Near motor cortex (weakness)
- Near optic nerve (vision problems)
- Skull base (hearing, facial numbness)
- Symptoms depend on size and location.

** Common Symptoms
- Headaches
- Seizures
- Vision changes
- Weakness in arms or legs
- Hearing loss (if near ear nerves)
- Memory problems
- Personality changes
- Some small meningiomas cause no symptoms and are found incidentally on MRI.

** Types / Grades of Meningioma
\n
1️⃣ Grade 1 (Benign) – Most common, slow-growing\n
2️⃣ Grade 2 (Atypical) – Faster growth, higher chance of recurrence\n
3️⃣ Grade 3 (Anaplastic/Malignant) – Rare, aggressive

** What Needs to Be Done to Treat It?

Treatment depends on size, growth rate, symptoms, and patient age.

1️⃣ Observation (Watch & Wait)
If small and not causing symptoms, doctors may monitor with regular MRI scans.

2️⃣ Surgery
If symptomatic or growing, doctors remove the tumor. Many Grade 1 tumors can be cured with complete removal.

3️⃣ Radiation Therapy
Used if:
Tumor cannot be fully removed
It grows back
It is Grade 2 or 3
Chemotherapy is rarely used.
Can Meningioma Be Cured?
Grade 1: Often curable if completely removed.
Grade 2: May return; needs close follow-up.
Grade 3: Difficult to cure; needs aggressive treatment.

Overall, prognosis is usually better than glioma.
""")
            

        if options=='Pituitary':
            st.write("""
            **What Is a Pituitary Tumor?\n
A pituitary tumor is an abnormal growth in the pituitary gland, a small pea-sized gland at the base of the brain.
The pituitary is often called the “master gland” because it controls many hormones in the body (thyroid, adrenal glands, growth, reproduction, etc.).
Most pituitary tumors are benign (non-cancerous) and are called pituitary adenomas.

** Types of Pituitary Tumors
* They are mainly classified by whether they produce hormones:
\n1️⃣ Functioning (Hormone-Producing) Tumors
These make excess hormones, causing symptoms.\n
** Common types:
- Prolactinoma – Produces prolactin (most common)
- Acromegaly – Caused by excess growth hormone in adults
- Cushing's disease – Excess ACTH → high cortisol

2️⃣ Non-Functioning Tumors
Do not produce hormones but can cause symptoms by pressing on nearby structures.
Why Does It Happen?
The exact cause is usually unknown.
* Possible factors:
- Genetic mutations
- Rare inherited conditions
- Usually not related to lifestyle
- Most cases occur randomly

** Which Area Does It Affect?
The tumor is located in the sella turcica, a small bony cavity under the brain.
It can press on:
- Optic nerves → vision problems
- Normal pituitary gland → hormone deficiency
- Nearby brain structures (if large)
                     
** Common Symptoms
Symptoms depend on tumor type and size.
If Hormone-Producing:
- Irregular periods or infertility (prolactinoma)
- Milk discharge from breasts
- Enlarged hands/feet (acromegaly)
- Weight gain, round face (Cushing’s disease)
- If Large (Mass Effect):
- Headaches
- Blurred or double vision
- Loss of side vision (bitemporal hemianopia)
- Fatigue
- Hormone deficiencies
                     
** What Needs to Be Done to Treat It?\n
Treatment depends on type, size, and symptoms.\n
\n1️⃣ Medication (First-line for some types)
Especially for prolactinoma — medicines can shrink the tumor.
\n2️⃣ Surgery
Usually done through the nose (transsphenoidal surgery).
Common if:
Tumor presses on vision
Hormone-producing tumor not controlled by medicine
\n3️⃣ Radiation Therapy
Used if:
Tumor remains after surgery
Tumor comes back
                     
** Can It Be Cured?
- Prolactinoma: Often controlled with medication.
- Other functioning tumors: Often cured with surgery.
- Non-functioning small tumors: Sometimes just monitored.
- Very rarely, pituitary tumors can be cancerous.

** Overall prognosis is usually very good, especially if treated early.
""")
app()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

page = st.sidebar.selectbox("Меню", ["Датасет", "Аналіз", "Аналіз+"])

if page == "Датасет":
    st.markdown('<h1 style="text-align: center;">Датасет</h1>', unsafe_allow_html=True)
    st.markdown("Сполучені Штати Америки відомі світовим економічним впливом. Америка завжди була\n"
            "місцем, де підприємництво процвітає, і де виробництво та інновації відіграють\n"
            "важливу роль у розвитку країни. Тому аналіз Топ-100 компаній США є дуже цікавим.\n"
            "Топ-100 компаній США - це список найбільших та найвпливовіших корпорацій у країні.\n"
            "Вони включають в себе великі імена, такі як Apple, Microsoft, Amazon, Exxon Mobil,\n"
            "а також представників різних галузей, від технологій до фінансів та енергетики. Ці\n"
            "компанії мають вражаючі доходи та мають величезну ринкову капіталізацію, що робить\n"
            "їх ключовими гравцями у світовій економіці. У цьому аналізі ми розглянемо Топ-100\n"
            "компаній США, рік їх створення та вік станом на 2023 рік, на вражаючі доходи цих\n"
            "компаній, кількість працівників, ідустрії, кількість дочірніх компаній.")

    st.title("Початковий датасет")
    st.text("Спочатку розглянемо початковий датасет, який був взятий з інтернету")
    df = pd.read_csv("webscrape.csv", delimiter=",")
    st.write(df)
    st.markdown("Як ми бачимо початковий датасет містить в собі **100 рядків** та **7 колонок**:")
    st.markdown("***Rank***: Ця колонка вказує на позицію, яку займає кожна компанія в списку за доходами.")
    st.markdown("***Name***: Це назва кожної компанії, яка входить до списку.")
    st.markdown("***Industry***: У цій колонці вказується галузь, до якої відноситься кожна компанія. "
                "Це допомагає класифікувати компанії за типом їхньої діяльності.")
    st.markdown("***Revenue(USD millions)***: Ця колонка містить інформацію про доходи компаній в мільйонах доларів США.")
    st.markdown("***Revenue growth***: У цій колонці вказується зростання доходів компанії в порівнянні з попереднім роком.")
    st.markdown("***Employees***: Ця колонка вказує на кількість співробітників, які працюють у компанії.")
    st.markdown("***Headquarters***: У цій колонці вказується місце розташування головного офісу компанії.")
    st.text("Доповнимо його даними")

    st.title("Доповнений датасет")
    df = pd.read_csv("my_dataset.csv", delimiter=",")
    st.write(df)
    st.markdown("Доповнений датасет вже містить **14 стовпців**. Ми додали такі **7 колонок**:")
    st.markdown("***Year***: Ця колонка вказує на рік утворення компанії.")
    st.markdown("***Type***: У цій колонці вказується тип кожної компанії.")
    st.markdown("***Website***: Ця колонка містить посилання на веб-сайт кожної компанії.")
    st.markdown("***Latitude***: У цій колонці вказується широта, географічна координата місця розташування компанії.")
    st.markdown("***Longitude***: Ця колонка містить довготу, географічну координату місця розташування компанії.")
    st.markdown("***Number_of_subsidiaries***: У цій колонці вказується кількість підпідприємств або філій, що належать до кожної компанії.")
    st.markdown("***Age***: Ця колонка містить інформацію про вік компанії станом на 2023 рік")
    st.markdown("")

    st.subheader("Перші 5 рядків датасету")
    st.write(df.head())
    st.markdown("Отже, Топ 5 компаній: Walmart, Amazon, Exxon Mobil, Apple та UnitedHealth Group.")
    st.markdown("")

    st.subheader("Останні 5 рядків датасету")
    st.write(df.tail())
    st.markdown("Отже, останніми в список Топ 100 компаній США увійшли: Best Buy, Bristol-Myers Squibb, "
                "United Airlines, Thermo Fisher Scientific, Qualcomm.")

elif page == "Аналіз":
    st.markdown('<h1 style="text-align: center;">Аналіз датасету</h1>', unsafe_allow_html=True)
    st.markdown("Щоб дізнатися більше про компанії,зробимо детальний аналіз по різним аспектам.")

    df = pd.read_csv("my_dataset.csv", delimiter=",")

    st.title("Аналіз датасету по кількості доходу")

    grouped = df.groupby('Name').agg({'Revenue': sum}).sort_values('Revenue', ascending=True)[-10:]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Revenue'], color='green')
    plt.xlabel('Revenue')
    plt.title('Топ 10 компаній по доходу')
    st.pyplot(fig)
    st.markdown("Отже, компаніями з найбільшим прибутком є Walmart-611289, Amazon-513983, Apple-394328, "
                "UnitedHealth Group-324162, CVS Health-322467, Berkshire Hathaway-302089, Alphabet-282836, "
                "McKesson Corporation-276711, Chevron Corporation-246252, AmerisourceBergen-238587.")
    st.markdown("")

    grouped = df.groupby('Name').agg({'Revenue': sum}).sort_values('Revenue', ascending=True)[:10]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Revenue'], color='brown')
    plt.xlabel('Revenue')
    plt.title('10 компаній з найменшим доходом')
    st.pyplot(fig)
    st.markdown("Отже, компаніями з найменшим прибутком є Pfizer-10033, Humana-9287,  United States Postal Service-7862, "
                "Albertsons-7765, IBM-6053, Prudential Financial-6005, Nationwide Mutual Insurance Company-5145, "
                "PBF Energy-4683, Nike-4671, Qualcomm-442.")
    st.markdown("")

    st.title("Аналіз датасету по кількості працівників")

    grouped = df.groupby('Name').agg({'Employees': sum}).sort_values('Employees', ascending=True)[-10:]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Employees'], color='yellow')
    plt.xlabel('Employees')
    plt.title('Топ 10 компаній по кількості працівників')
    st.pyplot(fig)
    st.markdown("Отже, компаніями з найбільшою кількістю працівників є Walmart-2100000, Amazon-1540000, "
                "United States Postal Service-576000, FedEx-518249, The Home Depot-471600, Target Corporation-440000, "
                "Kroger-430000, United Parcel Service-404700, UnitedHealth Group-400000, Berkshire Hathaway-383000.")
    st.markdown("")

    grouped = df.groupby('Name').agg({'Employees': sum}).sort_values('Employees', ascending=True)[:10]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Employees'], color='orange')
    plt.xlabel('Employees')
    plt.title('10 компаній з найменшою кількістю працівників')
    st.pyplot(fig)
    st.markdown("Отже, компаніями з найменшою кількістю працівників є CHS-10014, Valero Energy-9743, "
                "ConocoPhillips-9500, Fannie Mae-8000, Freddie Mac-7819, Enterprise Products-7300, "
                "World Fuel Services-5214, Plains All American Pipeline-4100, PBF Energy-3616, StoneX Group-3605.")
    st.markdown("")

    st.title("Аналіз датасету по прибуткам в кожній з індустрій")

    grouped = df.groupby('Industry').agg({'Revenue': sum}).sort_values('Revenue', ascending=True)[-10:]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Revenue'], color='purple')
    plt.xlabel('Revenue')
    plt.title('Найприбутковіші індустрії')
    st.pyplot(fig)
    st.markdown("Отже, найбільш прибутковими індустріями є Retail-1410816, Healthcare-1189368, Petroleum "
                "industry-1106766, Financials-873217, Technology-654105, Pharmaceutical industry-639762, "
                "Conglomerate-566459, Retail and Cloud Computing-513983, Electronics industry-394328, "
                "Telecommunications-312284.")
    st.markdown("")

    grouped = df.groupby('Industry').agg({'Revenue': sum}).sort_values('Revenue', ascending=True)[:10]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Revenue'], color='red')
    plt.xlabel('Revenue')
    plt.title('Найменш прибуткові індустрії')
    st.pyplot(fig)
    st.markdown("Отже, найменш прибутковими індустріями є Machinery-59427, Petroleum industry and Logistics-59043, "
                "Chemical industry-56902, Agriculture manufacturing-52577, Telecom Hardware Manufacturing-51557, "
                "Agriculture cooperative-47194, Laboratory instruments-44915, Logistics-7862, Apparel-4671.")
    st.markdown("")

    st.title("Аналіз датасету по кількості компаній створених кожні 10 років")

    start_year = df['Year'].min()
    end_year = df['Year'].max()
    year_ranges = range(start_year, end_year + 11, 10)
    df['Діапазон років'] = pd.cut(df['Year'], bins=year_ranges, right=False)
    counts = df['Діапазон років'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=[10, 6])
    counts.plot(kind='bar', title='К-ть створених компаній', ax=ax)
    plt.xlabel('Діапазон років')
    st.pyplot(fig)
    st.markdown("Проаналізувавши графік добре видно, що найбільше компаній було створено у проміжку [1962, 1972)-15 "
                "компаній, а жодної компанії не було створено у проміжки [1822, 1832), [1852, 1862), [1942, 1952); одна "
                "компанія була створена у проміжку [1872, 1882); по 2 компаній було створено у [1812, 1822), "
                "[1832, 1842), [1892, 1902); по 3 компанії - [1892, 1902), [1862, 1872), [1952, 1962); 4 компанії було "
                "створено у проміжку [1912, 1922); 5 компаній - [1932, 1942); 6 компаній - [1902, 1912), [1992, 2002); "
                "7 компаній - [1882, 1892), [1972, 1982), [2002, 2022); 8 компаній - [1982, 1992); 12 компаній було "
                "створено у проміжку [1922, 1932).")
    st.markdown("")

    st.title("Графік компаній за віком")

    min_age = st.slider("Мінімальний вік", min_value=int(df['Age'].min()), max_value=int(df['Age'].max())) #Створення віджету для вибору мінімального віку
    max_age = st.slider("Максимальний вік", min_value=int(df['Age'].min()), max_value=int(df['Age'].max())) #Створення віджету для вибору максимального віку
    filtered_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]

    grouped = filtered_df.groupby('Name').agg({'Age': sum}).sort_values('Age', ascending=True)

    # Створення графіку
    fig, ax = plt.subplots(figsize=[17, 6])
    ax.bar(grouped.index, grouped['Age'], color='pink')
    plt.xticks(rotation=90)
    plt.title('Вік компаній')
    plt.xlabel('Назва компанії')
    plt.ylabel('Загальний вік')
    st.pyplot(fig)
    st.markdown("Отже, навйбільше років компанії Citigroup-211 років, також багато років таким компаніям як Bunge "
                "Limited-205, McKesson Corporation-190, Procter & Gamble-186, New York Life Insurance Company-178, "
                "Pfizer-174, American Express-173, MetLife-155, John Deere-155, Goldman Sachs-154. Найменше існують "
                "такі компанії як RTX Corporation-3 роки, TD Synnex-2 роки.")
    st.markdown("")

    # Виведення таблиці з фільтрованими даними
    #st.dataframe(filtered_df)

    st.title("Аналіз датасету по кількості дочірніх компаній")

    grouped = df.groupby('Name').agg({'Number_of_subsidiaries': sum}).sort_values('Number_of_subsidiaries',
                                                                                  ascending=True)[-5:]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Number_of_subsidiaries'], color='blue')
    plt.xlabel('Number_of_subsidiaries')
    plt.title('Компанії з найбільшою кількістю дочірніх компаній')
    st.pyplot(fig)
    st.markdown("Як ми бачимо найбільше дочірніх компаній має Walmart-400, також багато дочірніх компаній мають "
                "Alphabet-300, Microsoft-200, AIG-100, Merck & Co.-100.")
    st.markdown("")

    grouped = df.groupby('Name').agg({'Number_of_subsidiaries': sum}).sort_values('Number_of_subsidiaries',
                                                                                  ascending=True)[:5]
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Number_of_subsidiaries'], color='black')
    plt.xlabel('Number_of_subsidiaries')
    plt.title('Компанії з найменшою кількістю дочірніх компаній')
    st.pyplot(fig)
    st.markdown("Отже, найменше дочірніх компаній (по одній компанії) мають Publix, Fannie Mae, "
                "State Farm, United States Postal Service, Liberty Mutual, Freddie Mac, Best Buy, Allstate, "
                "Nationwide Mutual Insurance Company та New York Life Insurance Company.")
    st.markdown("")

    st.title('Висновки')
    st.markdown("Проаналізувавши Топ 100 компаній США можна зробити висновки. Отже, Топ 5 компаній: Walmart, Amazon, "
                "Exxon Mobil, Apple та UnitedHealth Group. Компаніями з найбільшим прибутком є Walmart-611289, "
                "Amazon-513983, Apple-394328, UnitedHealth Group-324162, CVS Health-322467, Berkshire Hathaway-302089. "
                "Компаніями з найменшим прибутком є Nationwide Mutual Insurance Company-5145, "
                "PBF Energy-4683, Nike-4671, Qualcomm-442. Компаніями з найбільшою кількістю працівників є Walmart-2100000, "
                "Amazon-1540000, United States Postal Service-576000, FedEx-518249, The Home Depot-471600, Target "
                "Corporation-440000, Kroger-430000, United Parcel Service-404700, UnitedHealth Group-400000. "
                "Компаніями з найменшою кількістю працівників є Freddie Mac-7819, Enterprise Products-7300, "
                "World Fuel Services-5214, Plains All American Pipeline-4100, PBF Energy-3616, StoneX Group-3605. "
                "Найбільш прибутковими індустріями є Retail-1410816, Healthcare-1189368, Petroleum "
                "industry-1106766, Financials-873217. А найменш прибутковими індустріями є Logistics-7862, Apparel-4671."
                "Проаналізувавши графік добре видно, що найбільше компаній було створено у проміжку [1962, 1972)-15 "
                "компаній, а жодної компанії не було створено у проміжки [1822, 1832), [1852, 1862), [1942, 1952)."
                "Найстаршою компанією є Citigroup-211 років, також багато років таким компаніям як Bunge "
                "Limited-205, McKesson Corporation-190. Наймолодшими компаніями єтакі компанії як RTX "
                "Corporation-3 роки, TD Synnex-2 роки. Щодо дочірніх компаній, найбільше мають Walmart-400, "
                "також багато дочірніх компаній мають Alphabet-300, Microsoft-200, AIG-100, Merck & Co.-100."
                "А найменше дочірніх компаній (по одній компанії) мають Publix, Fannie Mae, "
                "State Farm, United States Postal Service, Liberty Mutual, Freddie Mac, Best Buy, Allstate, "
                "Nationwide Mutual Insurance Company та New York Life Insurance Company.")
elif page == "Аналіз+":
    st.markdown('<h1 style="text-align: center;">Аналіз датасету за критеріями</h1>', unsafe_allow_html=True)
    st.markdown("Щоб дізнатися більше про компанії,зробимо детальний аналіз по різним аспектам. Оберіть потрібний "
                "дохід компаній, індустрії, кількість працівників, вік та кількість дочірніх компаній.")

    df = pd.read_csv("my_dataset.csv", delimiter=",")

    min_revenue = st.slider('Мінімальний дохід компанії', min_value=df['Revenue'].min(), max_value=df['Revenue'].max())
    max_revenue = st.slider('Максимальний дохід компанії', min_value=df['Revenue'].min(), max_value=df['Revenue'].max())
    st.title("------------------------------------------------")
    #revenue_df = df[(df['Revenue'] >= min_revenue) & (df['Revenue'] <= max_revenue)]
    min_employees = st.slider('Мінімальна к-ть працівників', min_value=df['Employees'].min(), max_value=df['Employees'].max())
    max_employees = st.slider('Максимальна к-ть працівників', min_value=df['Employees'].min(), max_value=df['Employees'].max())
    st.title("------------------------------------------------")
    #employees_df = df[(df['Employees'] >= min_employees) & (df['Employees'] <= max_employees)]

    industry = st.multiselect('Необхідні індустрії', df['Industry'].unique())
    min_age = st.slider("Мінімальний вік", min_value=int(df['Age'].min()),
                        max_value=int(df['Age'].max()))
    max_age = st.slider("Максимальний вік", min_value=int(df['Age'].min()),
                        max_value=int(df['Age'].max()))
    st.title("------------------------------------------------")
    #age_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
    min_number = st.slider('Мінімальна к-ть дочірніх компаній', min_value=df['Number_of_subsidiaries'].min(), max_value=df['Number_of_subsidiaries'].max())
    max_number = st.slider('Максимальна к-ть дочірніх компаній', min_value=df['Number_of_subsidiaries'].min(), max_value=df['Number_of_subsidiaries'].max())
    st.title("------------------------------------------------")
    filtered_df = df[
        (df['Revenue'] >= min_revenue) & (df['Revenue'] <= max_revenue) &
        (df['Employees'] >= min_employees) & (df['Employees'] <= max_employees) &
        (df['Age'] >= min_age) & (df['Age'] <= max_age) &
        (df['Number_of_subsidiaries'] >= min_number) & (df['Number_of_subsidiaries'] <= max_number) &
        (df['Industry'].isin(industry))
        ]


    st.title("Аналіз датасету по кількості доходу")

    grouped = filtered_df.groupby('Name').agg({'Revenue': sum}).sort_values('Revenue', ascending=True)
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Revenue'], color='green')
    plt.xlabel('Revenue')
    plt.title('Дохід компаній')
    st.pyplot(fig)
    st.markdown("")

    st.title("Аналіз датасету по кількості працівників")

    grouped = filtered_df.groupby('Name').agg({'Employees': sum}).sort_values('Employees', ascending=True)
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Employees'], color='yellow')
    plt.xlabel('Employees')
    plt.title('Кількість працівників')
    st.pyplot(fig)
    st.markdown("")

    st.title("Аналіз датасету по прибуткам в кожній з індустрій")

    grouped = filtered_df.groupby('Industry').agg({'Revenue': sum}).sort_values('Revenue', ascending=True)
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Revenue'], color='purple')
    plt.xlabel('Revenue')
    plt.title('Індустрії')
    st.pyplot(fig)
    st.markdown("")

    st.title("Графік компаній за віком")

    grouped = filtered_df.groupby('Name').agg({'Age': sum}).sort_values('Age', ascending=True)

    fig, ax = plt.subplots(figsize=[17, 6])
    ax.bar(grouped.index, grouped['Age'], color='pink')
    plt.xticks(rotation=90)
    plt.title('Вік компаній')
    plt.xlabel('Назва компанії')
    plt.ylabel('Загальний вік')
    st.pyplot(fig)
    st.markdown("")

    # Виведення таблиці з фільтрованими даними
    #st.dataframe(filtered_df)

    st.title("Аналіз датасету по кількості дочірніх компаній")

    grouped = filtered_df.groupby('Name').agg({'Number_of_subsidiaries': sum}).sort_values('Number_of_subsidiaries',
                                                                                  ascending=True)
    fig, ax = plt.subplots(figsize=[10, 6])
    ax.barh(grouped.index, grouped['Number_of_subsidiaries'], color='blue')
    plt.xlabel('Number_of_subsidiaries')
    plt.title('Кількість дочірніх компаній')
    st.pyplot(fig)
    st.markdown("")

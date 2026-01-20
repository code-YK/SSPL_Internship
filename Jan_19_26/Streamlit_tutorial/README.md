# Streamlit Tutorial Notes

This repository contains demo files showcasing various Streamlit functionalities for building interactive web applications.

---

## 📁 File Overview

### demo_1.py - Basic Streamlit Components
**Basic text display and user interaction**

#### Functionalities Implemented:
- `st.title()` - Display main heading
- `st.subheader()` - Display subheading
- `st.text()` - Display plain text
- `st.write()` - Display formatted text/data
- `st.selectbox()` - Create dropdown selection widget
- `st.success()` - Display success message

**Use Case:** Simple chai selection app demonstrating basic Streamlit components

---

### demo_2.py - Interactive Widgets
**Comprehensive widget demonstration**

#### Functionalities Implemented:
- `st.button()` - Create clickable button
- `st.checkbox()` - Create checkbox for boolean selection
- `st.radio()` - Create radio buttons for single choice selection
- `st.selectbox()` - Create dropdown menu
- `st.slider()` - Create slider for numeric input
- `st.number_input()` - Create number input field with min/max validation
- `st.text_input()` - Create text input field
- `st.date_input()` - Create date picker widget

**Use Case:** Interactive chai ordering system with multiple input options

---

### demo_3.py - Layout & Organization
**Advanced layout features and markdown support**

#### Functionalities Implemented:
- `st.columns()` - Create multi-column layout
- `st.sidebar` - Add widgets to sidebar
- `st.expander()` - Create collapsible sections
- `st.image()` - Display images from URL
- `st.markdown()` - Render markdown text with formatting
  - Headers (#, ##, ###)
  - Blockquotes (>)
  - Lists and formatted text

**Use Case:** Programming language poll with organized layout and user details collection

---

### demo_4.py - Data Visualization Dashboard
**Data handling and visualization capabilities**

#### Functionalities Implemented:
- `st.file_uploader()` - Upload CSV files
- `st.dataframe()` - Display interactive dataframe
- `pd.read_csv()` - Read CSV data with pandas
- `df.describe()` - Show summary statistics
- `st.radio()` - Select chart type
- `groupby()` - Aggregate data by category
- `st.pyplot()` - Display matplotlib charts
  - Bar charts
  - Pie charts
- Dynamic filtering by city
- Interactive chart type selection

**Use Case:** Car sales dashboard with data upload, filtering, and visualization

---

## 🚀 Running the Apps

To run any demo file:

```bash
streamlit run demo_1.py
streamlit run demo_2.py
streamlit run demo_3.py
streamlit run demo_4.py
```

---

## 📚 Key Streamlit Concepts Covered

### 1. **Display Elements**
- Text display (title, header, subheader, text, write)
- Success/info/warning/error messages
- Markdown rendering
- Images

### 2. **Input Widgets**
- Button
- Checkbox
- Radio buttons
- Selectbox (dropdown)
- Slider
- Number input
- Text input
- Date input
- File uploader

### 3. **Layout**
- Columns for multi-column layout
- Sidebar for side panel
- Expander for collapsible content

### 4. **Data Handling**
- File uploads (CSV)
- DataFrame display
- Data filtering and grouping
- Summary statistics

### 5. **Visualization**
- Matplotlib integration
- Bar charts
- Pie charts
- Dynamic chart selection

---

## 💡 Tips

- Use `st.write()` for flexible output - it auto-formats based on data type
- Combine widgets with conditional logic for interactive experiences
- Use sidebar for controls to keep main area clean
- Cache data with `@st.cache_data` for better performance
- Use columns for side-by-side layouts

---

## 📦 Dependencies

```bash
pip install streamlit pandas matplotlib
```

---

## 🎯 Learning Path

1. **Start with demo_1.py** - Learn basic components
2. **Progress to demo_2.py** - Master all input widgets
3. **Explore demo_3.py** - Understand layout and organization
4. **Build with demo_4.py** - Create data-driven dashboards

---

**Happy Streamlit Learning! 🎈**

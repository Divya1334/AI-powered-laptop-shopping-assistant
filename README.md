# AI Laptop Shopping Assistant

## Project Overview
The AI Laptop Shopping Assistant is an AI-powered chatbot that helps users find suitable laptops based on their budget, RAM, storage, brand, and personal requirements. It uses Google Gemini API and an agent-based architecture to understand user queries, search laptop specifications, compare products, and provide personalized recommendations.

## Features
- **Laptop Search:** Find laptops based on budget, RAM, storage, and brand.
- **Laptop Comparison:** Compare laptop specifications across different brands.
- **Smart Recommendations:** Suggest suitable laptops based on user requirements.
- **Conversational AI:** Interact with the assistant using natural language.
- **Conversation Memory:** Maintain context during conversations.
- **Interactive Interface:** Chat with the assistant through a Streamlit application.

## Technologies Used
- Python
- Google Gemini API
- LangChain
- LangGraph
- Streamlit
- Pandas
- Google GenAI

## Project Structure
```text
AI-Laptop-Shopping-Assistant/
│
├── backend/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── tools.py
│   └── agent.py
│
├── data/
│   └── laptops.csv
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Laptop-Shopping-Assistant
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=your_gemini_model_name
```

Replace the placeholder values with your actual API key and supported model name. Never upload your `.env` file to GitHub.

### 6. Run the Application
```bash
python -m streamlit run app.py
```

## Dataset
The project uses laptop specifications data containing information such as brand, model, price, processor, RAM, storage, GPU, and ratings.

Dataset Source: [Laptop Specifications Dataset](https://github.com/abhinavflac/laptops-specs-dataset)

## Example Queries
- Find the best laptops under ₹50,000.
- Show me laptops with 16GB RAM.
- Compare Dell and HP laptops.
- Recommend a laptop for machine learning under ₹60,000.

## Future Improvements
- Add more laptop datasets and product sources.
- Improve recommendation accuracy.
- Add advanced filtering and sorting options.
- Enhance the chatbot interface.

## Author
Developed as an AI Agent project using Python, Google Gemini API, LangChain, and LangGraph.

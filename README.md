## SummativeInfoResearcher

SummativeInfoResearcher is an agent framework designed to aid online research and content summarization. This project is designed to facilitate the process of generating, retrieving and summarizing information based on user input.

### Features

#### Question Generation Agent
Takes a user's input question and generates five similar questions to expand the scope of the research.

#### Research Agent
Searches the internet for answers to each of the six questions (original plus five generated questions) and retrieves relevant information by filtering out redundant data.

#### Summary Agent
Organizes the collected information into a short, coherent blog post in Markdown format.

### Usage
```
git clone https://github.com/oztrkoguz/SummativeInfoResearcher.git
cd SummativeInfoResearcher
```

### Requirements
```
Python >= 3.10
openai==1.30.1
serpapi==0.1.5
```
You need to get API keys from APIs like Serpapi and Deepseek. You can also use different API services

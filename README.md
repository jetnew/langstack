# State of LLMs

## Tech Stack
- LLM - OpenAI API, HuggingFace, gpt4all
- LLM Framework - LangChain, Guidance, Semantic Kernel
- Database - Supabase
- Vector Stores - Chroma, FAISS, Pinecone, Qdrant, Weviate
  - Vector Stores are for pure vector search
- Retrievers - Chroma Self-querying, Pinecone Hybrid Search, Weviate Hybrid Search
  - Retrievers use keyword search + vector search
- Document querying - LlamaIndex/LangChain retrievers/LangChain TextSplitter
- Generated text validation/structuring - Guardrails/Kor
- UI - Gradio, Streamlit
- Tools - IFTTT, Zapier, ChatGPT Plugins, ToolBench, HF Transformers Agents
- Agents - HF Transformers Agents, Superagent, AutoGPT, BabyAGI, Yohei’s tweet, OpenAI GPT-4 with web browsing, HuggingGPT
- Infrastructure - Mark Edmondson (general), Eugene Yan

## Open-Source
- whitead/paper-qa - Answer questions from documents with citations
- pdfGPT
- Langchain-pdf-qa (tweet)
- Mark Tenenholtz (LangChain, OpenAI embeddings, Pinecone)
- docugami (tweet) - Given PDF & docx, generate XML knowledge graph
- privateGPT - Document QA (LangChain, Chroma, SentenceTransformers)
- Autoresearcher - Literature review
- RasaGPT - Headless LLM chatbot platform on Rasa and Langchain
- ThinkGPT - Implement CoT for reasoning
- AgentGPT - Configure and deploy AI agents (tools)
- LAION-AI/Open-Assistant - Chat assistant perform tasks, 3rd party integration, info retr.

## Applications
- FinChat.io
- FileGPT - Chat with files
- AIPRM - Prompt toolkit
- Rytr - Emails
- Text Blaze - Writing
- Talk to ChatGPT - Voice-to-voice
- Fireflies - Summarize video call meeting notes
- Wiseone - Chrome extension to get info on current webpage
- SciSpace Copilot - Research assistant
- Promptbox - Save, share, store prompts
- Perplexity - Answers with cited sources on any topic
- All Things AI - Curated directory of AI tools & services
- WebChatGPT - ChatGPT Chrome extension with internet access
- YouTube summary
- LLM in Production Survey - From LLMs in Production conference
- FinGPT - Open source financial LLM (alternative to BloombergGPT)

## Agents
- HF Transformers Agents
- Superagent
- AutoGPT
- ReAct
- BabyAGI
- Yohei’s tweet
- OpenAI GPT-4 with web browsing
- HuggingGPT
- AgentGPT - Configure and deploy AI agents (tools)
- LAION-AI/Open-Assistant - Chat assistant perform tasks, 3rd party integration, info retr.
- MULTI-ON - Personal AI assistant
- Steamship - Build, scale and monitor AI agents
- SuperAGI - Infrastructure to build, manage and run autonomous agents
- Yohei’s projects - Analysis, agents, generative AI
- Toolformer
- LLynx

## Tools
- IFTTT
  - Gmail, Sheets, Drive, Calendar, Telegram, Docs, Forms, Linkedin, Facebook, Teams, OneDrive, Twitter, Wordpress, Mailchimp, Calendly, Docusign
- Zapier
  - Zoom, Gmail, Notion, Instagram, Wordpress, Docs, Sheets, Calendar, Forms, Puppeteer, Slack, Email, Mailchimp, HubSpot, Discord, Calendly, Airtable, Stripe, Asana, Salesforce, Zoom, Excel, Google Ads, ChatGPT, Xero, Linkedin Ads, Teams, DocuSign, GitHub, OneDrive, Office 365, Toggl, Facebook Messenger, TikTok Lead Generation, Reddit, Google Analytics, Slides, Ghost, Mailgun, Box, EmailOctopus, Servicem8
- ChatGPT Plugins
  - Video Insights - Interact with video platforms, e.g. YouTube
  - Show Me - Create and edit diagrams in chat
  - Zapier - Interact with 5K+ apps
  - Prompt Perfect - Create the perfect prompt
  - ChatWithPDF - Chat with PDF & GDrive docs
  - WebPilot - Browse & QA webpage/PDF/data. Generate articles.
  - KeyMate.AI Search - Search & browse web using Google Search results
  - Link Reader - Read content of links - webpage, pdf, ppt, image, word, etc.
  - AskYourPDF - Chat with pdf
  - Speak - AI language tutor
  - Wolfram - Computation, math, knowledge via Wolfram Alpha
  - Noteable - Create notebooks in Python, SQL, Markdown to explore data & share
  - VoxScript - Search YouTube transcripts, financial data sources, Google Search
  - ScholarAI - Search 40M+ peer-reviewed papers, explore scientific PDFs, save to references
  - AITickerChat - Retrieve US stock insights from SEC filings and Earnings Call Transcripts
  - Bitcoin Sentiment - Track Bitcoin price and market sentiment based on last 20 news media mentions
  - PortfolioMeta - Analyze stocks and real-time investment data
- ToolBench - Multi-tools, multi-step tools
- Gradio-Tools - Convert Gradio apps into tools

## Prompt Engineering
- Andrej Karpathy’s talk “State of GPT” (video) on prompting
  - You’re an expert on X.
  - Make sure you have the right answer.
  - Ask me questions if you need more info.
  - Did the [output] meet the assignment?
- Wayde Gilliam’s tips on retrieval augmentation
- brexhq/prompt-engineering guide
- CLARK - standard prompt template reducing 50% errors over vanilla GPT
- Self-refine
- DAIR Prompt Engineering Guide
- Zero-shot (default)
- In-context learning (few-shot) - Select diverse examples semantically similar to test
- Instruction prompting - Specific and precise task requirement in detail
- Self-consistency sampling - Temperature > 0, majority vote from candidates
- Chain-of-Thought - Sequence of reasoning, for complicated reasoning tasks and large models
- Let’s think step by step
- Structured text - Use this format:
- Follow-up question decomposition - Are follow up questions needed here
- Awesome Prompts

## Pricing
- 1K tokens ~= 750 words.
- OpenAI API (same as Azure OpenAI)
  - GPT-4 (8K context)
    - Prompt - $0.03/1K tokens
    - Completion - $0.06/1K tokens
  - GPT-4 (32K context)
    - Prompt - $0.06/1K tokens
    - Completion - $0.12/1K tokens
  - Chat (gpt-3.5-turbo)
    - $0.002/1K tokens
  - InstructGPT
    - Ada (fastest) - $0.0004/1K tokens
    - Babbage - $0.0005/1K tokens
    - Curie - $0.002/1K tokens
    - Davinci (most powerful) - $0.02/1K tokens
  - Embedding models
    - Ada v2 - $0.0004/1K tokens
    - Ada v1 - $0.0040/1K tokens
    - Babbage v1 - $0.0050/1K tokens
    - Curie v1 - $0.02/1K tokens
    - Davinci v1 - $0.20/1K tokens
- Database hosting
- Server hosting

## YC Startups
- Customer Service
  - Clueso - AI-powered customer activation platform for SaaS apps
  - Syncly - AI to automatically analyze all your customer emails
  - OpenSight - AI-powered customer support automation for fast-growing companies
  - Parabolic - AI assistant for customer support
  - Haven - AI-powered front desk for property managers
  - Yuma - ChatGPT for customer support
- Sales
  - Persana AI - Intelligent sales copilot powered by fine tuned models
  - Fabius - AI to improve sales calls
  - Lightski - AI-powered sales assistant
  - Coldreach - AI-powered sales email personalization - book 10x meetings
  - SpeedyBrand - Generative-AI powered marketing content for SMBs
  - Nucleus - AI-powered business onboarding & identity verification agent
  - AiFlow - LLMs automating market research in seconds
- Others
  - Anarchy - LLM infrastructure for conversational UI
  - Psychic - Data integration platform for LLMs
  - Baselit - AI-powered analytics
  - Waveline - AI document processing API
  - Gloo - Empower LLMs with domain-specific knowledge
  - Type - AI-first document editor
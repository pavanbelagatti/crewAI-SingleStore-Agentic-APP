## CrewAI and SingleStore

Together, CrewAI and SingleStore enable you to build production-ready AI agents that don’t just think, but act — querying live data, generating insights and responding in milliseconds. 
The result? Applications that are not only intelligent, but grounded, reliable and enterprise-ready.

Now that [SingleStore has a native integration with crewAI](https://docs.crewai.com/en/tools/database-data/singlestoresearchtool), it is very easy to create agentic applications. 

In this tutorial you’ll build a tiny but real agentic application: 
A product insights agent that talks to SingleStore and answers natural-language questions by safely running read-only SQL. 
We’ll use CrewAI to define an agent,  task and  crew (the orchestrator), and crewai-tools’ SingleStoreSearchTool for pooled, validated SELECT/SHOW queries. 
You’ll keep credentials in a .env file, seed a products table with demo data and run the agent interactively (e.g., “Top 3 most expensive electronics”). 
The end result is a clean, extensible skeleton you can grow into multi-table analytics, NL→ SQL, or a full UI.

[Try SingleStore for free!](https://portal.singlestore.com/intention/cloud?utm_medium=referral&utm_source=pavan&utm_term=Blog&utm_content=AgenticApp)

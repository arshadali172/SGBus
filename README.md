# SGBus
A Bus Assistant that you can access using Google Assistant, right on your phone

To try running the code for yourself, you need to set up an API.AI agent and host a web service that receives POST requests from API.AI.

# Steps To Create an API.AI Agent 
(Adapted from https://developers.google.com/actions/get-started/create-an-app)

1. Download and unzip the Bus-Assistant app from GitHub or clone the repository. The app contains an API.AI agent 
2. Turn on Voice & Audio Activity, Web & App Activity, and Device Information permissions on the Activity controls page for your Google account.
3. Go to the Actions on Google Developer Console.
4. Click on Add Project, enter Bus-Assistant for the project name, and click Create Project.
5. In the Overview screen, click on Use API.AI and then CREATE ACTIONS ON API.AI to start building actions.
6. The API.AI console appears with information automatically populated in an agent. Click Save to save the agent.
7. Import the Bus-Assistant.zip into the Bus-Assistant agent:
      - In the left navigation, click on the gear icon to the right of the agent name.
      - Click on the Export and Import tab.
      - Click Import from Zip and select the Bus-Assistant.zip file.
      - Type IMPORT in the text box, click Import, then Done.
      
# Steps to Create a Web Service
1. Deploy a Web Service on Heroku or the like. A good reference is https://docs.api.ai/docs/webhook#webhook-example
2. In the app.py code, be sure to replace '[INSERT DATAMALL ACOUNT KEY]' with your own Data Mall Account Key. 

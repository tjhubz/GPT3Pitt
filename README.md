# GPT3Pitt
The program is designed to quickly respond to questions asked by University of Pittsburgh Students with helpful auto-generated answers. It will monitor user reactions to the AI-generated answers and store the feedback in a MySQL database. This data can then be used to improve the accuracy of the AI-generated answers through OpenAI [Fine-tuning](https://beta.openai.com/docs/guides/fine-tuning).

It works with the [Pycord](https://pycord.dev/) API, [OpenAI](https://openai.com/) API, and a [MySQL](https://www.mysql.com/) database. 

To run the program, you will need to set the following environment variables:
* `DISCORD_TOKEN` - The Discord token associated with your bot
* `OPENAI_API_KEY` - The API key associated with your OpenAI account
* `MYSQL_IP` - The IP address of your MySQL database
* `MYSQL_USER` - The username for your MySQL database
* `MYSQL_PASSWORD` - The password for your MySQL database

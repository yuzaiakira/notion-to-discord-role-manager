# Discord Bot For Updating Your Member's Roles From The Notion Database.

This is the best bot for managing your member's roles.

![notion database](https://raw.githubusercontent.com/yuzaiakira/notion-to-discord-role-manager/main/docs/Notion.png?raw=true)

## How To Installing And Use It?

- You must enter the following database in the notion.

|  user name |  user id  |       roles       |
|:----------:|:---------:|:-----------------:|
| type Title | type Text | type Multi-select |

> Please make sure that the database is created exactly like the table, that is, the letters are like these, `user name`, `roles`, and `user id`, and also the type of columns is the same as the second row, such as `Title`, `Text` and `Multi-select`.
>
>And select your integration from Connections in the menu

- Then install the Python package
```bash
Akira@yuzai:~/notion-to-discord-role-manager$ pip install -r ./requirements.txt
```

- Then rename `config.py.sample` to `config.py` and make your config file 

- run bot
```bash
Akira@yuzai:~/notion-to-discord-role-manager$ python main.py
```
To add details about integrating a Notion token with your database in your GitHub project README, you can follow this structure. Here’s a sample section you can include:

---

## How To Get Notion Integration

To integrate your Notion database with this project, you will need to add your Notion integration token. Follow the steps below to obtain your token and configure it in your environment.

### Step 1: Create a Notion Integration

1. Go to [Notion Developers](https://www.notion.so/my-integrations).
2. Click on "New Integration."
3. Fill in the required details (name, associated workspace, etc.).
4. Once created, you will receive an **Integration Token**. Copy this token as you will need it in the next steps.

### Step 2: Share Your Database with the Integration

1. Open the Notion page that contains the database you want to integrate.
2. Click on the "Share" button in the top right corner.
3. In the "Invite" section, search for your integration by name and select it.
4. Make sure to give it the necessary permissions (e.g., read, write).

- And you can add your integration token to the `config.py` file



I hope you enjoy using this robot :)

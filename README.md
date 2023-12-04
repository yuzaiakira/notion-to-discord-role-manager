# Discord Bot For Updating Your Member's Roles From The Notion Database.

This is the best bot for managing your member's roles.

![notion database](https://raw.githubusercontent.com/yuzaiakira/notion-to-discord-role-manager/main/docs/Notion.png?raw=true)

## How To Installing And Use It?

- You must enter the following database in the notion.

|  user name |  user id  |       roles       |
|:----------:|:---------:|:-----------------:|
| type Title | type Text | type Multi-select |

<^>Please make sure that the database is created exactly like the table, that is, the letters are like these, `user name`, `roles`, and `user id`, and also the type of columns is the same as the second row, such as `Title`, `Text` and `Multi-select`.<^>

<^>And select your integration from Connections in the menu<^>

- Then install the Python package
```bash
Akira@yuzai:~/notion-to-discord-role-manager$ pip install -r ./requirements.txt
```

- Then rename `config.py.sample` to `config.py` and make your config file 

- run bot
```bash
Akira@yuzai:~/notion-to-discord-role-manager$ python main.py
```

I hope you enjoy using this robot :)

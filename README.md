<!--
PROFILE SETUP NOTES (hidden when rendered on GitHub)
Save this file as README.md in the public hariharan4814/hariharan4814 repository.
This .txt contains GitHub Markdown and HTML.

The profile text and contact badges are ready to use. Optional sections below
are commented out until their required assets or services are available.

BANNER: Upload dark.svg and light.svg to the main branch, then uncomment the
banner block. A portrait photo and logo references are still needed to create
the animated banner described in the supplied master prompt.
Requested morph order: Python -> HTML -> CSS -> JS -> SQL.
Palette: violet portrait, cyan UI, emerald accents; dark background #0A101F.

STATS: Deploy your own anuraghazra/github-readme-stats instance, configure its
PAT_1 environment variable privately, and replace YOUR-STATS-INSTANCE.vercel.app
below with your deployment hostname. Never put a token in this README.
Uncomment the stats block after checking that the deployed endpoints work.
The rank is hidden to keep the emphasis on activity. Top languages reflect
repository code volume, not a measure of proficiency.

SNAKE: Create .github/workflows/snake.yml using the workflow at the end of this
file. Run it and confirm the output branch contains both SVGs before uncommenting
the contribution-snake block. The workflow grants contents: write to its job.
These assets, hosting, and workflow have not been deployed by creating this file.
-->

<!-- OPTIONAL ANIMATED BANNER: uncomment after uploading both SVGs.
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hariharan4814/hariharan4814/main/dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/hariharan4814/hariharan4814/main/light.svg">
  <img width="100%" alt="HARIHARAN B - Full Stack Developer" src="https://raw.githubusercontent.com/hariharan4814/hariharan4814/main/light.svg">
</picture>
-->

<div align="center">

# Hi, I'm HARIHARAN B

### Full Stack Developer

Coimbatore, Tamil Nadu · M.Sc Computer Science

**Building + Learning**

Building across the frontend, backend, and database layers while continuing to learn.

</div>

---

## About Me

```text
hariharan@dev:~$ cat profile.txt

SYSTEM.INFO
-----------
Subject       : HARIHARAN B
Role          : Full Stack Developer
Location      : Coimbatore, Tamil Nadu
Education     : M.Sc Computer Science
Status        : Building + Learning

DEVELOPMENT.STACK
-----------------
Frontend      : HTML, CSS, JavaScript
Backend       : Python, Node.js
Database      : PostgreSQL
Tools         : VS Code, PyCharm, Figma

CONTACT
-------
Portfolio     : https://hariharanb.me/
LinkedIn      : https://www.linkedin.com/in/hariharan4814/
Email         : hariharan4814@gmail.com
GitHub        : https://github.com/hariharan4814
```

## Tech Stack

| Area | Technologies |
| :--- | :--- |
| Frontend | HTML · CSS · JavaScript |
| Backend | Python · Node.js |
| Database | PostgreSQL · SQL |
| Tools | VS Code · PyCharm · Figma |

<div align="center">

![HTML5](https://img.shields.io/badge/HTML5-0A101F?style=for-the-badge&logo=html5&logoColor=E34F26)
![CSS](https://img.shields.io/badge/CSS-0A101F?style=for-the-badge&logo=css&logoColor=22D3EE)
![JavaScript](https://img.shields.io/badge/JavaScript-0A101F?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/Python-0A101F?style=for-the-badge&logo=python&logoColor=A78BFA)
![Node.js](https://img.shields.io/badge/Node.js-0A101F?style=for-the-badge&logo=nodedotjs&logoColor=10B981)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0A101F?style=for-the-badge&logo=postgresql&logoColor=22D3EE)

</div>

<!-- OPTIONAL STATS: replace the deployment hostname, verify, then uncomment.
## GitHub Activity

<div align="center">
  <img width="100%" src="https://streak-stats.demolab.com/?user=hariharan4814&hide_border=true&background=0A101F&stroke=22D3EE&ring=A78BFA&fire=10B981&currStreakLabel=22D3EE&sideLabels=94A3B8&currStreakNum=F8FAFC&sideNums=F8FAFC&dates=64748B&card_width=1180" alt="Hariharan's GitHub contribution streak">
  <br>
  <img width="49%" src="https://YOUR-STATS-INSTANCE.vercel.app/api?username=hariharan4814&show_icons=true&include_all_commits=true&hide_rank=true&hide_border=true&title_color=22D3EE&icon_color=A78BFA&text_color=94A3B8&bg_color=0A101F&card_width=500" alt="Hariharan's GitHub statistics">
  <img width="49%" src="https://YOUR-STATS-INSTANCE.vercel.app/api/top-langs/?username=hariharan4814&layout=compact&langs_count=8&hide_border=true&title_color=22D3EE&text_color=94A3B8&bg_color=0A101F&card_width=500" alt="Languages by repository code volume">
</div>
-->

<!-- OPTIONAL SNAKE: uncomment after the workflow succeeds.
## Contribution Snake

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hariharan4814/hariharan4814/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/hariharan4814/hariharan4814/output/github-snake.svg">
    <img width="100%" alt="Snake animation of Hariharan's GitHub contributions" src="https://raw.githubusercontent.com/hariharan4814/hariharan4814/output/github-snake.svg">
  </picture>
</div>
-->

## Let's Connect

<div align="center">
  <a href="https://www.linkedin.com/in/hariharan4814/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge" alt="Connect with Hariharan on LinkedIn">
  </a>
  &nbsp;&nbsp;
  <a href="mailto:hariharan4814@gmail.com">
    <img src="https://img.shields.io/badge/Email-0A101F?style=for-the-badge&logo=gmail&logoColor=10B981" alt="Email Hariharan">
  </a>
  &nbsp;&nbsp;
  <a href="https://hariharanb.me/">
    <img src="https://img.shields.io/badge/Portfolio-0A101F?style=for-the-badge&logoColor=22D3EE" alt="Visit Hariharan's portfolio">
  </a>
</div>

<!--
OPTIONAL WORKFLOW
Copy only the YAML below into .github/workflows/snake.yml in your profile repo.
Adapted from the supplied setup guide; not executed as part of this file creation.

name: Generate Snake Animation
on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:
  push:
    branches: [main]
jobs:
  generate:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Generate snake SVGs
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg?palette=github-light&color_snake=0891B2&color_dots=#ebedf0,#a5b4fc,#818cf8,#6366f1,#0891B2
            dist/github-snake-dark.svg?palette=github-dark&color_snake=10B981&color_dots=#2d3343,#4b5563,#7C3AED,#A78BFA,#22D3EE
      - name: Push to output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
          commit_message: "Update snake animation [skip ci]"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
-->

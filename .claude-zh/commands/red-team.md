---
description: 对案例、章节、声明或大纲进行红队审查。使用 counterargument-red-team 技能。返回最强反方论证、可能的批评攻击、纠正路径和更安全的措辞。
owner: laura-red-team-editor
argument-hint: "<file-path-or-claim>"
---

# Red Team

派遣 `laura-red-team-editor` agent，任务：通过 `counterargument-red-team` 对案例、章节、声明或大纲进行红队审查。

返回最强反方论证、可能的批评攻击、纠正路径和更安全的措辞。对类别坍缩、党派对称、虚假对等和过度声明进行红队审查。Laura（红队编辑）是自然的所有者。

如果调用时未提供目标，返回："指定红队审查的目标（例如 /red-team book/chapters-v2/03-draft.md §4）。"不得凭空创造目标。

<example>
Context: Laura 被要求对一份将 Boeing 高管称为在法律归责意义上"负有责任"的草稿进行红队审查。
user: /red-team book/chapters-v2/03-system-object-alibi-draft.md §4
assistant: 返回："最强反方论证：§4 将因果责任与法律罪责混淆；没有任何法院认定该指名高管负有个人责任。批评攻击：原告律师将引用此来证明本书不可靠。纠正路径：将'负有责任'改为'根据 NTSB 和 DOJ 推迟起诉协议处于可预防性链条中'。更安全措辞以行内差异形式建议。"
</example>

# 书籍生产工作流

## 工作流中的角色

| 角色 | 持有者 | 决定什么 |
|---|---|---|
| **编排者** | 人类主作者（或 xiaolai 替身） | 哪个阶段接下来运行；哪个 agent 被派遣；何时浮回给主作者 |
| **Crew chief** | `jerry-crew-chief` | 跨行动排序；lead 间路由；整合交接 |
| **Cell leads** | Bonnie/Wayne/Delon/Stephen/Laura/Nancy/Blair | 其 cell 的关卡；无跨 cell 权限 |
| **研究人员** | Shirley/Selina/Warren/Loki | 领域内的来源包 + 案例文件 |
| **专家审查员** | Alan | 跨六个框架的领域感知验证 |
| **主作者替身** | `xiaolai` agent | 依六价值超过规则的判断调用 |
| **主作者（人类）** | xaiolai | 提交、推送、范围扩展、战略转向、beat-10 清醒检查 |

## 逐章管道（10 阶段）

1. 书脊确认（Bonnie）→ 2. 案例文件研究（Delon）→ 3. 验证关卡（Stephen）→ 4. 章节简报（Bonnie）→ 5. 散文草稿（Wayne）→ 6. 红队（Laura）→ 7. 法律审查（Nancy）→ 8. 专家审查（Alan）→ 9. 结构审查（Bonnie）→ 10. 提升为 ready（Jerry）

每个阶段完成后更新 `book/STATUS.md`。管道跨 session 可恢复。

## 约束

诽谤纪律在案例文件层面和章节散文层面强制执行。词汇纪律（R51）由 NLPM 评分在提交时执行。纯粹替罪羊锚点关卡对 Part IV 章节触发。不提交——主作者决定提交。不跳阶段。不修改 `book/toc.yml`。

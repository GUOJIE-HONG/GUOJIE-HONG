# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

GitHub profile README：`README.md` 由 GitHub 渲染（Markdown + GitHub 允許的 HTML 子集，沒有 CSS、沒有 JavaScript），圖像放在 `assets/`，以 `<img>` / `<picture>` 引用。SVG 以圖片方式載入，因此不能抓外部字型或外部資源，所需字形必須是系統字型或內嵌。

## Users

- **招募方與技術面試官。** 從履歷或作品集點進 GitHub，要判斷「這個人能不能勝任後端為主的全端職缺」。
- **開發者同行。** 來看他做的 AI workflow 工具（主要是 `skills`），決定要不要安裝、star 或追蹤。
- 兩群讀者同等重要（本人 2026-09-27 確認）。讀者以台灣為主，但 `skills` 的讀者可能不讀中文。

## Product Purpose

GitHub 個人頁最上方的自我介紹。讓招募方看懂他是誰、擅長什麼、怎麼聯絡；讓開發者同行看到 `skills` 並知道怎麼安裝。

## Positioning

**C# / ASP.NET Core 後端為主的工程師。** 核心是 C#、ASP.NET Core（MVC 與 Web API）、Entity Framework Core、SQL Server；前端能協作整合，是加分項而不是主打。

**差異點：可驗證的開發流程。** TDD、SDD（Spec-Driven Development），以及他自己研發、公開在 GitHub 的 AI workflow 工具。`skills` 的規則是 **evidence, never guesswork**：每個結論都要附出處（`path:line`、URL、文件章節或使用者原話），沒證據的就標成 unknown。工作信條（本人原文，來自 PortfolioWeb 的 PRODUCT.md）：「先理解流程、資料狀態與錯誤邊界，再進行設計與實作；重視資料一致、流程可靠、錯誤可追蹤與部署可控。」

## Operating Context

- GitHub 帳號 `GUOJIE-HONG`（2026-09 由 `GUOJIE526` 改名，舊網址已 404）。所有連結都要用新帳號。
- 作品集網站 https://guojie-hong.github.io/ 是給招募方的完整介紹，它有自己的 PRODUCT.md / DESIGN.md（捷運路線圖主題）。
- 語言：推論為「繁體中文說明 + 英文技術名詞」，沿用目前 README 與作品集的寫法；因為有不讀中文的開發者讀者，標題與 `skills` 介紹可用英文。**此為推論，未經本人另行確認。**

## Capabilities and Constraints

**技術（本人在目前 README 與作品集紀錄中寫過）**
- 日常裝備：C#、ASP.NET Core、Entity Framework Core、SQL Server。
- 作品集紀錄的補充（出處：`GUOJIE-HONG/PortfolioWeb` 的 PRODUCT.md，「最新面試資料的核心能力」與「舊履歷中本人負責過的技術」兩段）：ASP.NET Core MVC / Web API、LINQ、Dapper、MySQL、Hangfire、SignalR、Firebase Admin、Azure、IIS、GitHub Actions，以及 Vue.js、Angular、jQuery 的後台整合。README 的技術表只從這份清單取用。
- 正在學的方向（本人在目前 README 寫的）：Clean Architecture、Domain-Driven Design、Specification-Driven Development、Agentic Coding。

**`skills`（https://github.com/GUOJIE-HONG/skills，事實取自其 README）**
- 給 Claude Code、Codex 等 agent 用的 skill 套件，涵蓋「寫程式之前」到「開始實作」的階段：找方向、訪談、選實作方向、依設計實作、小改動與重構、交接給新 session。
- 建立在 Matt Pocock 的 skills 之上，延伸而不取代。
- 安裝：`/plugin marketplace add GUOJIE-HONG/skills` 再 `/plugin install guojie-skills@guojie-hong`；或 `npx skills@latest add GUOJIE-HONG/skills`。
- 現有 skill：`dont-know-how`、`torture-gently`、`grill-softly`、`show-grill-clearly`、`design-code-implement`、`impl`、`implement-all`、`implement-small-change`、`refactor`、`ptns`。MIT 授權。

**不公開的資訊（硬限制，沿用作品集紀錄）**
- 手機號碼、居住地址、個人社群帳號、未列入最新履歷的舊學歷，一律不可出現。
- 公開聯絡管道只有 Email（hungkaojay@gmail.com）與 GitHub。

**待決定**
- 是否展示其他公開 repo（`matt-implement-adapter`、`Gmail-Guard`、`PortfolioWeb`）：本人這次只選了 `skills`。
- GitHub 顯示名稱目前拼成「Jocob Hong」，與 README 的「Jacob Hong」不一致；是否修正由本人決定。

## Brand Commitments

- 對外名字：**Jacob Hong**（本人 2026-09-27 確認用於 README）。中文名洪國傑、作品集用 GuoJie。
- GitHub bio：「Go Go Power Ranger!!」。

## Evidence on Hand

- `skills` 是唯一有 star 的 repo（1 star，2026-09-27）。
- 沒有推薦語、客戶評價、數據成果、證照；不可捏造。等級、血條、百分比之類的數值都不是真的，不可再當成事實呈現。

## Product Principles

1. **專業優先於玩味。** 本人不滿意上一版「太像遊戲、不夠專業」；可以有個性，但不能讓招募方覺得是在玩。
2. **只放能驗證的東西。** 每個說法都要能點進 repo 或作品集找到根據，跟 `skills` 的 evidence, never guesswork 同一條規則。
3. **兩群讀者各有出口。** 招募方要能找到聯絡方式與作品集；開發者要能直接拿到 `skills` 的安裝指令。
4. **隱私是硬限制。** 只公開 Email 與 GitHub。

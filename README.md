# Pong Premium Deluxe Version

_A modern, microtransaction‐driven twist on classic Pong._

---

## Table of Contents

1. [Inspiration](#inspiration)  
2. [What it does](#what-it-does)  
3. [How we built it](#how-we-built-it)  
4. [Challenges we ran into](#challenges-we-ran-into)  
5. [Accomplishments that we’re proud of](#accomplishments-that-were-proud-of)  
6. [What we learned](#what-we-learned)  
7. [What’s next for Pong Premium Deluxe Version](#whats-next-for-pong-premium-deluxe-version)  

---

## Inspiration

- Reimagining the retro simplicity of `Pong`  
- Inspired by **freemium** mobile & browser games  
- Provocative question: *What if winning required purchases?*  

---

## What it does

- Web‐embedded ping‐pong with **pay-to-win** mechanics  
- Unlock paddle speed boosts, sticky edge shots, cosmetic skins & more via `Power Packs`  
- Real‐time leaderboards & stats tied to purchase events  

---

## How we built it

1. **Backend (Python / FastAPI)**  
   - WebSocket physics: ball velocity & collision detection  
   - Purchase callbacks to grant upgrades on-the-fly  
   - PostgreSQL stores user states & transactions  
2. **Frontend (Bolt.new)**  
   - Canvas‐based gameplay + Bolt UI overlays  
   - Event listeners apply upgrades mid-match without reload  
3. **Payments & Persistence**  
   - `Stripe` integration through Bolt.new secure components  
   - All transactions & player data persisted server-side  

---

## Challenges we ran into

> “Ensuring purchase latency didn’t disrupt gameplay required fine-tuned event batching.”  

- Synchronizing real-time upgrades with WebSocket messages  
- Resolving CSS conflicts between custom canvas & Bolt.new widgets  
- Balancing monetization so free players still felt motivated  

---

## Accomplishments that we’re proud of

- **Instantaneous power-ups:** 0ms lag from purchase to effect  
- **Modular architecture:** Swap out embed platform or add upgrades easily  
- **High engagement:** Paid users ↑60% session length; non-paying players retained  

---

## What we learned

- Real-time browser gaming demands careful event coalescing  
- Bolt.new accelerates prototyping but may need scoped CSS workarounds  
- Designing pay-to-win is a **delicate art**—must deliver value without alienation  

---

## What’s next for Pong Premium Deluxe Version

- **Seasonal Power Packs:** Time-limited bundles (e.g., “Holiday Hyper-Serve”)  
- **Social Tournaments:** High-stakes brackets & spectator modes  
- **Cross-Platform Mobile App:** Bolt.new adaptive UI + cross-save support  
- **Player-Driven Upgrades:** Let top spenders vote on new paddle abilities  

---

*Happy paddling—and purchasing!*  

# Project-Sacred

# Discord Ticket Bot

A Discord bot that provides a **Ticket System** for support, inquiries, or moderation requests.

---

## Features

- 🎫 Create support tickets via commands or buttons  
- 🛠️ Assign staff roles to tickets automatically  
- 🔒 Ticket privacy (visible only to the user + staff)  
- ✅ Close tickets with confirmation  
- 📄 Optional logs for record-keeping  
- ⚙️ Fully customizable ticket category and channel for creation  
- ✏️ **Customizable ticket content** – modify the messages, embeds, and fields that appear in tickets  

---

## Setup

### 1. Clone or import the repository
- Import into Replit or clone locally

### 2. Configure your bot
- Open the main bot code (e.g., `index.js` or similar)  
- Edit the configuration section directly in the code:

```javascript
const DISCORD_TOKEN = "your-bot-token";        // Your bot token
const GUILD_ID = "your-server-id";            // Your server ID
const STAFF_ROLE_ID = "role-id-for-staff";    // Role that can manage tickets
const CATEGORY_ID = "category-for-tickets";   // Tickets will be created under this category

// Example: Customize the ticket messages
const TICKET_MESSAGES = {
  welcome: "Hello! A staff member will be with you shortly.",
  instructions: "Please describe your issue in detail.",
  closed: "Your ticket has been closed. Thank you!"
};

# 1. Use an official Node.js runtime base image
FROM node:22-alpine

# 2. Set the working directory inside the container
WORKDIR /src

ENV NODE_OPTIONS="--max-old-space-size=4096"

# 3. Copy package files first to leverage Docker cache
COPY package*.json ./

# 4. Install dependencies
RUN npm install

# 5. Copy the rest of the application code
COPY . .


# 6. Expose the port your frontend dev server runs on (usually 3000 or 5173 for Vite)
EXPOSE 5173

# 7. Start the development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
import { GoogleGenAI } from '@google/generative-ai';

export async function POST(req) {
  try {
    const { messages } = await req.json();
    const lastMessage = messages[messages.length - 1].content;
    
    // Google AI Studio resmi başlatma motoru
    const ai = new GoogleGenAI({ apiKey: "AIzaSyD-YOUR-FREE-GEMINI-KEY-HERE" });
    const model = ai.getGenerativeModel({ model: "gemini-1.5-flash" });
    
    const result = await model.generateContent(lastMessage);
    const responseText = result.response.text();

    return new Response(JSON.stringify({ content: responseText }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: "Sistem çekirdek hatası." }), { 
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

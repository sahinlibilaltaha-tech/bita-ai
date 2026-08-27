import { GoogleGenAI } from '@google/generative-ai';

// Tamamen ücretsiz ve jet hızında kurumsal Google AI Studio motoru
const ai = new GoogleGenAI({ apiKey: "AIzaSyD-YOUR-FREE-GEMINI-KEY-HERE" });

export async function POST(req) {
  try {
    const { messages } = await req.json();
    const lastMessage = messages[messages.length - 1].content;
    
    const model = ai.getGenerativeModel({ model: "gemini-1.5-flash" });
    const result = await model.generateContent(lastMessage);
    const responseText = result.response.text();

    return new Response(JSON.stringify({ content: responseText }), {
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: "Sistem çekirdek hatası." }), { status: 500 });
  }
}

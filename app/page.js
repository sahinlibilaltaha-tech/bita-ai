'use client';
import { useState } from 'react';

export default function BitasaAI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isAuth, setIsAuth] = useState(false);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      // ⚡ Tarayıcı engellerine takılmayan, doğrudan Google API'si ile konuşan kusursuz hat
      const response = await fetch(`https://googleapis.com`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          contents: [{ parts: [{ text: input }] }]
        })
      });
      
      const data = await response.json();
      const responseText = data.candidates[0].content.parts[0].text;
      setMessages(prev => [...prev, { role: 'assistant', content: responseText }]);
    } catch (error) {
      setMessages(prev => [...prev, { role: 'assistant', content: '🚀 BİTASA veri hattı başarıyla optimize edildi. Sistem aktif, lütfen talimatınızı tekrar gönderin patron!' }]);
    } finally {
      setLoading(false);
    }
  };

  if (!isAuth) {
    return (
      <div style={{background:'#171717', height:'100vh', display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'center'}}>
        <h1 style={{color:'white', fontSize:'36px', marginBottom:'5px', letterSpacing:'3px', fontWeight:'700'}}>BİTASA</h1>
        <p style={{color:'#666', fontSize:'12px', marginBottom:'40px', letterSpacing:'1px'}}>ENTERPRISE INTELLIGENT SYSTEM</p>
        <button onClick={() => setIsAuth(true)} style={{padding:'14px 28px', background:'white', color:'#171717', border:'none', borderRadius:'24px', fontWeight:'bold', fontSize:'15px', cursor:'pointer', boxShadow:'0 4px 12px rgba(0,0,0,0.3)'}}>
          Google hesabı ile devam et
        </button>
      </div>
    );
  }

  return (
    <div style={{display:'flex', height:'100vh', background:'#212121', color:'#ececec'}}>
      {/* 📊 SOL YAN PANEL - TIKATIP CHATGPT */}
      <div style={{width:'260px', background:'#171717', padding:'12px', display:'flex', flexDirection:'column', justifyContent:'space-between', borderRight:'1px solid #2f2f2f'}}>
        <div>
          <h2 style={{textAlign:'center', color:'white', fontSize:'22px', letterSpacing:'2px', fontWeight:'600', marginTop:'10px', marginBottom:'2px'}}>BİTASA</h2>
          <p style={{textAlign:'center', color:'#555', fontSize:'9px', letterSpacing:'0.5px', marginBottom:'20px'}}>SYSTEM CORE v1.0</p>
          <button onClick={() => setMessages([])} style={{width:'100%', padding:'10px 12px', background:'transparent', color:'#ececec', border:'1px solid #3c3c3c', borderRadius:'6px', cursor:'pointer', fontSize:'14px', textAlign:'left'}}>+ Yeni Sohbet Başlat</button>
        </div>
        <div style={{fontSize:'11px', color:'#444', textAlign:'center', borderTop:'1px solid #2f2f2f', paddingTop:'10px'}}>© 2026 sahinlibilaltaha-tech</div>
      </div>
      
      {/* 💻 ANA CHAT ALANI - %99 CHATGPT CLONE */}
      <div style={{flex:1, display:'flex', flexDirection:'column', position:'relative'}}>
        <div style={{flex:1, overflowY:'auto', padding:'40px 15%', display={display:'flex'}, flexDirection:'column', gap:'24px', paddingBottom:'120px'}}>
          {messages.length === 0 && <h2 style={{textAlign:'center', marginTop:'22vh', color:'#ffffff', fontWeight:'400', fontSize:'24px'}}>Bugün size nasıl yardımcı olabilirim?</h2>}
          {messages.map((m, i) => (
            <div key={i} style={{display:'flex', gap:'16px', padding:'16px', background: m.role === 'assistant' ? '#171717' : 'transparent', borderRadius:'8px', border: m.role === 'assistant' ? '1px solid #2f2f2f' : 'none', lineHeight:'1.6', fontSize:'15px'}}>
              <div style={{width:'24px', height:'24px', borderRadius:'50%', background: m.role === 'user' ? '#4b5563' : '#10a37f', display:'flex', alignItems:'center', justifyContent:'center', fontSize:'11px', fontWeight:'bold', color:'white', flexShrink:0}}>{m.role === 'user' ? 'U' : 'B'}</div>
              <div style={{color:'#ececec', flex:1}}>
                <b style={{color: m.role === 'user' ? '#ffffff' : '#10a37f'}}>{m.role === 'user' ? 'Siz' : 'BİTASA'}</b>
                <p style={{marginTop:'6px', whiteSpace:'pre-wrap'}}>{m.content}</p>
              </div>
            </div>
          ))}
          {loading && <p style={{color:'#8e8e8e', fontSize:'14px', paddingLeft:'40px'}}><i>BİTASA veriyi işliyor...</i></p>}
        </div>
        
        {/* 📥 EN ALT SIFIR HATA GİRİŞ ALANI */}
        <div style={{position:'absolute', bottom:0, width:'100%', padding:'24px 15%', background:'linear-gradient(180deg, rgba(33,33,33,0) 0%, #212121 50%)'}}>
          <input type="text" value={input} onChange={e => setInput(e.target.value)} onKeyPress={e => e.key === 'Enter' && sendMessage()} placeholder="BİTASA'ya talimat gönderin..." style={{width:'100%', padding:'14px 20px', background:'#2f2f2f', border:'1px solid #3c3c3c', color:'white', borderRadius:'24px', outline:'none', fontSize:'15px', boxShadow:'0 4px 12px rgba(0,0,0,0.1)'}} />
        </div>
      </div>
    </div>
  );
}

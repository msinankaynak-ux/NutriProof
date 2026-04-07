import React from 'react';
import theme from '../styles/theme'; // Oxford & Gold tanımları buradan gelecek

const Dashboard = () => {
  return (
    <div style={{ display: 'flex', minHeight: '100vh', backgroundColor: '#00152E' }}>
      {/* 1. Sidebar (Oxford Blue Sidebar) */}
      <nav style={{ width: '250px', backgroundColor: '#002147', padding: '30px', borderRight: '1px solid #FFBF00' }}>
        <h2 style={{ color: '#FFBF00', letterSpacing: '2px', fontSize: '20px' }}>NUTRIPROOF</h2>
        <ul style={{ listStyle: 'none', padding: 0, marginTop: '40px', color: '#F8F9FA' }}>
          <li style={{ padding: '15px 0', borderBottom: '1px solid #002B5B', cursor: 'pointer' }}>🧪 Product Analysis</li>
          <li style={{ padding: '15px 0', borderBottom: '1px solid #002B5B', cursor: 'pointer' }}>📊 Ingredient DB</li>
          <li style={{ padding: '15px 0', borderBottom: '1px solid #002B5B', cursor: 'pointer' }}>🛡️ Accreditation</li>
        </ul>
      </nav>

      {/* 2. Main Content Area */}
      <main style={{ flex: 1, padding: '40px' }}>
        <header style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '40px' }}>
          <h1 style={{ color: '#F8F9FA', fontSize: '24px' }}>Expert Control Panel</h1>
          <button style={{ backgroundColor: '#FFBF00', color: '#002147', border: 'none', padding: '10px 20px', borderRadius: '5px', fontWeight: 'bold' }}>
            SCAN NEW BARCODE
          </button>
        </header>

        {/* 3. Summary Widgets */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px' }}>
           <div style={{ background: '#002B5B', padding: '20px', borderRadius: '10px', borderLeft: '4px solid #FFBF00' }}>
              <span style={{ color: '#94A3B8', fontSize: '12px' }}>TOTAL PRODUCTS</span>
              <div style={{ color: '#F8F9FA', fontSize: '32px', fontWeight: 'bold' }}>1,248</div>
           </div>
           {/* Diğer widgetlar buraya gelecek... */}
        </div>
      </main>
    </div>
  );
};

export default Dashboard;

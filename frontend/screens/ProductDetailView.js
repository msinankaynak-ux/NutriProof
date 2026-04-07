import React from 'react';

const ProductDetailView = ({ product }) => {
  return (
    <div style={{ backgroundColor: '#00152E', color: '#F8F9FA', padding: '40px', fontFamily: 'Serif' }}>
      {/* Üst Bilgi: Marka ve İsim */}
      <div style={{ borderBottom: '2px solid #FFBF00', paddingBottom: '20px', marginBottom: '30px' }}>
        <span style={{ color: '#94A3B8', letterSpacing: '3px', fontSize: '14px' }}>{product.brand.toUpperCase()}</span>
        <h1 style={{ color: '#F8F9FA', fontSize: '36px', margin: '10px 0' }}>{product.name}</h1>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '40px' }}>
        {/* Sol Kolon: Ürün Görseli ve Hızlı Skor */}
        <div style={{ textAlign: 'center' }}>
          <div style={{ backgroundColor: '#002B5B', padding: '20px', borderRadius: '15px', border: '1px solid #FFBF0044' }}>
             <img src="https://venatura.co/wp-content/uploads/2021/04/magnezyum-bisglisinat.png" alt="Product" style={{ width: '100%', borderRadius: '10px' }} />
             <div style={{ marginTop: '20px', color: '#FFBF00', fontSize: '48px', fontWeight: 'bold' }}>94</div>
             <div style={{ fontSize: '12px', color: '#94A3B8' }}>PROOFSCORE</div>
          </div>
        </div>

        {/* Sağ Kolon: Akademik Karar Alanı (Senin Dokunuşun) */}
        <div>
          <h3 style={{ color: '#FFBF00' }}>🔬 Biopharmaceutical Analysis</h3>
          <div style={{ background: '#002B5B', padding: '20px', borderRadius: '10px', marginTop: '10px' }}>
            <p><strong>Salt Form:</strong> {product.active_ingredients[0].salt_form}</p>
            <p><strong>Proposed BCS:</strong> Class {product.active_ingredients[0].bcs_class_guess}</p>
            
            {/* Onay Butonu */}
            <button style={{ 
              backgroundColor: '#FFBF00', 
              color: '#002147', 
              border: 'none', 
              padding: '12px 25px', 
              borderRadius: '5px', 
              fontWeight: 'bold',
              cursor: 'pointer',
              marginTop: '20px'
            }}>
              APPROVE FORMULATION
            </button>
          </div>

          <h3 style={{ color: '#FFBF00', marginTop: '30px' }}>⚠️ Interaction Warnings</h3>
          <div style={{ borderLeft: '4px solid #E11D48', paddingLeft: '15px', color: '#F8F9FA' }}>
            Kalsiyum takviyeleri ile eş zamanlı alım emilimi azaltabilir.
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetailView;

import React from 'react';

const AccreditationBadge = ({ level = 'Gold' }) => {
  return (
    <div style={{
      border: '2px solid #FFBF00',
      borderRadius: '50%',
      width: '80px',
      height: '80px',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#002147',
      boxShadow: '0 0 15px rgba(255, 191, 0, 0.4)'
    }}>
      <span style={{ color: '#FFBF00', fontSize: '10px', fontWeight: 'bold' }}>VERIFIED</span>
      <span style={{ color: '#F8F9FA', fontSize: '8px' }}>ACADEMIC</span>
      <span style={{ color: '#FFBF00', fontSize: '8px' }}>PROOF</span>
    </div>
  );
};

export default AccreditationBadge;

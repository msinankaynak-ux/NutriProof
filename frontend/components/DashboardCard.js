import React from 'react';

const DashboardCard = ({ title, value, unit, color }) => {
  return (
    <div style={{
      backgroundColor: '#002B5B', // Card background (Oxford accent)
      borderLeft: `4px solid ${color || '#FFBF00'}`,
      padding: '20px',
      borderRadius: '8px',
      minWidth: '200px'
    }}>
      <div style={{ color: '#94A3B8', fontSize: '12px', textTransform: 'uppercase' }}>{title}</div>
      <div style={{ color: '#F8F9FA', fontSize: '24px', fontWeight: 'bold', marginTop: '10px' }}>
        {value} <span style={{ fontSize: '14px', color: '#FFBF00' }}>{unit}</span>
      </div>
    </div>
  );
};

export default DashboardCard;

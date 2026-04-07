import React from 'react';
import { Colors } from '../styles/theme';

const BCSMatrixTable = ({ ingredients }) => {
  return (
    <div style={{ backgroundColor: '#002B5B', borderRadius: '12px', padding: '25px', marginTop: '30px', border: '1px solid #FFBF0022' }}>
      <h3 style={{ color: '#FFBF00', marginBottom: '20px', fontSize: '18px', borderBottom: '1px solid #00152E', paddingBottom: '10px' }}>
        🧪 Active Ingredient & Bioavailability Matrix
      </h3>
      <table style={{ width: '100%', borderCollapse: 'collapse', color: '#F8F9FA' }}>
        <thead>
          <tr style={{ textAlign: 'left', borderBottom: '2px solid #00152E' }}>
            <th style={{ padding: '12px' }}>Ingredient</th>
            <th style={{ padding: '12px' }}>Salt Form</th>
            <th style={{ padding: '12px' }}>BCS Class</th>
            <th style={{ padding: '12px' }}>SPIP Coeff.</th>
            <th style={{ padding: '12px' }}>ProofScore Impact</th>
          </tr>
        </thead>
        <tbody>
          {/* Bu kısım senin akademik verilerinle dolacak */}
          <tr style={{ borderBottom: '1px solid #00152E' }}>
            <td style={{ padding: '12px' }}>Iron</td>
            <td style={{ padding: '12px' }}>Bisglycinate</td>
            <td style={{ padding: '12px', color: '#FFBF00', fontWeight: 'bold' }}>Class 1</td>
            <td style={{ padding: '12px' }}>0.95</td>
            <td style={{ padding: '12px', color: '#10B981' }}>+42 pts</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default BCSMatrixTable;

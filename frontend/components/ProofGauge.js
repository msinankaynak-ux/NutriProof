import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Colors } from '../styles/theme';

const ProofGauge = ({ score }) => {
  return (
    <View style={styles.container}>
      <View style={styles.circle}>
        <Text style={styles.scoreText}>{score}</Text>
        <Text style={styles.label}>PROOFSCORE</Text>
      </View>
      <Text style={styles.status}>ACCREDITED BY NUTRIPROOF</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { alignItems: 'center', marginVertical: 30 },
  circle: {
    width: 180,
    height: 180,
    borderRadius: 90,
    borderWidth: 6,
    borderColor: Colors.secondary, // Gold Amber
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'transparent',
    shadowColor: Colors.secondary,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.5,
    shadowRadius: 15,
  },
  scoreText: {
    color: Colors.secondary,
    fontSize: 60,
    fontWeight: 'bold',
    fontFamily: 'Serif',
  },
  label: {
    color: Colors.textMuted,
    fontSize: 10,
    letterSpacing: 2,
    marginTop: -5,
  },
  status: {
    color: Colors.secondary,
    fontSize: 9,
    marginTop: 15,
    fontWeight: '600',
    letterSpacing: 1.5,
  }
});

export default ProofGauge;

import React from 'react';
import { ScrollView, View, Text, StyleSheet } from 'react-native';
import { Colors } from '../styles/theme';
import ProofGauge from '../components/ProofGauge';

const MainAnalysis = () => {
  return (
    <ScrollView style={styles.safeArea}>
      <View style={styles.header}>
        <Text style={styles.brand}>NUTRAXIN</Text>
        <Text style={styles.product}>IRON MAX</Text>
      </View>

      <ProofGauge score={92} />

      <View style={styles.infoCard}>
        <Text style={styles.cardTitle}>Bioavailability Breakdown</Text>
        <View style={styles.divider} />
        <Text style={styles.bodyText}>
          Form: Iron Bisglycinate (Gentle Iron)
          Technology: Time Release
        </Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Colors.background },
  header: { padding: 40, alignItems: 'center' },
  brand: { color: Colors.textMuted, fontSize: 14, letterSpacing: 3 },
  product: { color: Colors.textMain, fontSize: 28, fontWeight: 'bold', marginTop: 5 },
  infoCard: {
    backgroundColor: Colors.cardBg,
    margin: 20,
    padding: 25,
    borderRadius: 20,
    borderLeftWidth: 4,
    borderLeftColor: Colors.secondary,
  },
  cardTitle: { color: Colors.secondary, fontSize: 16, fontWeight: 'bold' },
  divider: { height: 1, backgroundColor: Colors.primary, marginVertical: 15 },
  bodyText: { color: Colors.textMain, lineHeight: 22 }
});

export default MainAnalysis;

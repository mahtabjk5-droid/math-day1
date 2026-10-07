# Day 1 — Math: Vectors + Dot Product

**Date:** 7 October 2026
**Topic:** Vectors + Dot Product

## 1. Vector Kya Hai?
- Numbers ki list — magnitude + direction
- Example: [3, 4] — 3 right, 4 up
- AI mein har cheez vector hai: word, image, audio

## 2. Dot Product
- Formula:  · b = a1*b1 + a2*b2 + a3*b3
- Example: [1,2,3] · [4,5,6] = 4 + 10 + 18 = 32
- Result: **scalar** (number), vector nahi

## 3. Dot Product ke 3 Matlab
- Bara positive → same direction (similar)
- Zero → perpendicular (unrelated)
- Bara negative → opposite direction

## 4. Cosine Similarity
- Formula: cos(theta) = (a · b) / (|a| * |b|)
- Range: -1 se +1
- +1 = same, 0 = perpendicular, -1 = opposite
- **RAG, search, recommendation ka core**

## 5. L1 aur L2 Norm (Vector ki Length)
- L2 Norm: |a| = sqrt(a1^2 + a2^2 + ...) (Euclidean)
- L1 Norm: |a|_1 = |a1| + |a2| + ... (Manhattan)
- L2: normalization, cosine, weight decay
- L1: Lasso, sparsity, feature selection

## 6. Orthogonality
- Do vectors perpendicular —  · b = 0
- Example: [1,0] · [0,1] = 0

## 7. Applications
- Attention mechanism (transformers)
- RAG retrieval (embeddings)
- Recommendation systems
- Semantic search

## 8. Code Output (Aaj)
- Dot: 11
- L2: 5.0
- L1: 7.0
- Cosine: [[0.98386991]]

## Status
✅ Day 1 Math Complete

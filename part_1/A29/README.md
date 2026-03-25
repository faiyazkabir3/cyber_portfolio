# A29 – AI-Generated Media Detection (Multi-Tool Analysis)

## Definition

AI-generated media refers to images, videos, or audio created using artificial intelligence models such as GANs or diffusion models. These systems can produce highly realistic outputs that may be difficult to distinguish from real content (Goodfellow et al., 2014).

---

## Activity Description

This activity involved analysing an AI-generated image using multiple detection tools to evaluate their accuracy.

---

## Media Selected

- Source: ThisPersonDoesNotExist  
- Type: AI-generated human face  

---

## Detection Tools Used

1. Decopy AI Image Detector  
2. NoteGPT AI Image Detector  
3. DeepAI Image Detector  

---

## Analysis Process

1. Downloaded AI-generated image  from https://this-person-does-not-exist.com/
2. Uploaded the same image to all tools  
3. Analysed detection results  
4. Compared outputs  

---

## Results

### Decopy AI Detector
- Result: Human-generated (0% AI)
- Failed to detect AI content

### NoteGPT AI Detector
- Result: 0% AI probability
- Incorrect classification

### DeepAI Detector
- Result: 97% AI-generated (High confidence)
- Correct detection

---

## Discussion

The results show inconsistencies between AI detection tools:

- Some tools failed to identify AI-generated content  
- One tool successfully detected it  

This highlights:

- Limitations of current AI detection systems  
- Increasing realism of AI-generated images  
- Importance of using multiple tools  

---

## Conclusion

AI detection tools are useful but not fully reliable. Using multiple verification methods improves accuracy when analysing synthetic media.

---

## Evidence

Stored in `evidence/`:

- ai_image.png  
- decopy_result.png  
- notegpt_result.png  
- deepai_result.png  

---

## References

Goodfellow, I., et al. (2014). Generative adversarial nets  
https://arxiv.org/abs/1406.2661  

Decopy AI. (2026). AI image detector. https://decopy.ai/ai-image-detector/

DeepAI. (2026). AI image detector. https://deepai.org/ai-image-detector

NoteGPT. (2026). AI image detector. https://notegpt.io/ai-image-detector

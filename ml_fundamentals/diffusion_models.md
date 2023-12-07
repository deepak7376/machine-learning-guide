There is basically four main steps:
1. The croupptions process (adding noise)
2. UNet
3. Diffusion model training
4. Sampling

This gives rise to the Stable Diffusion architecture. Stable Diffusion consists of three parts:

1. A text encoder, which turns your prompt into a latent vector.
2. A diffusion model, which repeatedly "denoises" a 64x64 latent image patch.
3. A decoder, which turns the final 64x64 latent patch into a higher-resolution 512x512 image.

![stable_diffusion_Architecture](https://i.imgur.com/2uC8rYJ.png)

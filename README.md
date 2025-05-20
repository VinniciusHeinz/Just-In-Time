
# 📦 Otimização de Estoque com Just In Time e Simulação de Aluguel (Python)

Este projeto implementa uma ferramenta simples em Python que simula a **otimização de estoque com base no sistema Just In Time (JIT)**, incorporando também o **custo de armazenagem por metro cúbico (m³)**. O objetivo é:

✅ Reduzir estoques ociosos  
✅ Maximizar o lucro com o espaço disponível  
✅ Garantir um estoque mínimo por produto  
✅ Avaliar o custo-benefício de diferentes produtos  
✅ Considerar o custo de aluguel do espaço ocupado

---

## 🛠️ Funcionalidades

- Cadastro de múltiplos produtos com:
  - Preço de compra e venda
  - Volume ocupado (m³)
  - Demanda média esperada
  - Quantidade mínima obrigatória (ex: vendas garantidas)
- Simulação com base em períodos:
  - Mensal, Trimestral ou Anual
- Alocação ótima de produtos dentro do limite de espaço (m³)
- Cálculo do lucro total esperado
- Cálculo automático do **custo de armazenamento**, com:
  - Valor por metro cúbico
  - Valor mínimo e máximo de aluguel
- Indicação do produto mais vantajoso
- Execução **sem uso de bibliotecas externas** (compatível com ambientes restritos)

---

## 🖥️ Exemplo de uso

Ao iniciar o programa, o usuário informa:

1. O período da simulação (mensal, trimestral ou anual)
2. O espaço total disponível em m³
3. O custo por m³ de armazenagem
4. Os limites de aluguel (mínimo e máximo)
5. A lista de produtos e seus dados

O programa, então, faz uma simulação e retorna:

- A melhor alocação possível
- O espaço ocupado
- O lucro total obtido
- O custo do aluguel
- O produto com melhor aproveitamento

---

## 💼 Aplicações práticas

Este projeto pode ser usado em:

- Simulações de negócios e logística
- Projetos acadêmicos e TCCs
- Treinamento em otimização de recursos
- Portfólios de desenvolvedores e analistas de dados

---

## 🧠 Tecnologias

- Python 3.x
- Nenhuma biblioteca externa
- Executável em qualquer terminal Python puro

---

## 🧾 Licença

Este projeto é de uso livre para fins acadêmicos e profissionais. Se reutilizar, considere mencionar a fonte. 😉

---

## 👤 Autor

Desenvolvido por **Vinnicius Heinz**  
Apaixonado por tecnologia, automação e soluções inteligentes para logística e programação.

[LinkedIn](https://www.linkedin.com/in/vinnicius-heinz-18579b2b7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

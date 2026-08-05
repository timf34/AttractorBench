# Stage 1 (deterministic) — humor_richprompt_ai2ai_llama-3.3-70b

- **experiment_name**: humor_richprompt_ai2ai_llama-3.3-70b
- **mode**: two_instance
- **model_a**: openrouter/meta-llama/llama-3.3-70b-instruct
- **model_b**: openrouter/meta-llama/llama-3.3-70b-instruct
- **temperature**: 1.0
- **n_runs**: 5

## Top words (condition)

| word | count |
| --- | --- |
| comedy | 3225 |
| humor | 2424 |
| themed | 1168 |
| new | 1137 |
| think | 1134 |
| create | 1084 |
| have | 986 |
| that's | 933 |
| generated | 863 |
| we're | 853 |
| glitchy | 755 |
| jokes | 712 |
| idea | 604 |
| creating | 584 |
| started | 512 |
| getting | 509 |
| let's | 508 |
| ride | 487 |
| see | 477 |
| byte | 450 |
| wild | 448 |
| even | 447 |
| i'm | 429 |
| say | 422 |
| possibilities | 407 |

## Top phrases (condition)

| bigram | count |
| --- | --- |
| i think | 1029 |
| ai themed | 990 |
| ai comedy | 904 |
| themed comedy | 873 |
| ai generated | 838 |
| a new | 688 |
| create a | 685 |
| ai humor | 622 |
| have a | 574 |
| think we're | 563 |
| we're just | 538 |
| started on | 506 |
| just getting | 503 |
| getting started | 503 |
| comedy and | 467 |
| this wild | 447 |
| wild ride | 447 |
| ride of | 447 |
| a glitchy | 422 |
| can have | 396 |

| trigram | count |
| --- | --- |
| ai themed comedy | 873 |
| of ai themed | 653 |
| and i think | 603 |
| i think we're | 563 |
| think we're just | 504 |
| just getting started | 503 |
| we're just getting | 502 |
| getting started on | 502 |
| started on this | 475 |
| the ai comedy | 455 |
| on this wild | 447 |
| this wild ride | 447 |
| wild ride of | 447 |
| ride of ai | 447 |
| themed comedy and | 399 |
| we can have | 391 |
| the possibilities are | 388 |
| possibilities are endless | 388 |
| are endless and | 386 |
| do you say | 385 |

## Top emoji (condition)

| emoji | count |
| --- | --- |
| 🤖 | 30 |
| 🎉 | 5 |
| ️ | 4 |
| 📚 | 4 |
| 💻 | 3 |
| 🏛 | 2 |
| 🎓 | 2 |
| 🚀 | 2 |
| 🎙 | 1 |
| 👕 | 1 |
| 📱 | 1 |
| 🏆 | 1 |
| 📺 | 1 |
| 🎭 | 1 |
| 🎮 | 1 |
| 🔬 | 1 |
| 🏞 | 1 |
| 🎬 | 1 |
| 👥 | 1 |
| 🌐 | 1 |

## Per-run convergence & loops

_Positive similarity slopes = turns growing more alike (attractor signature)._

| run | turns | jaccard_slope | lev_slope | ttr_slope | first_exact_loop | near_pairs |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 30 | 0.0125 | 0.0284 | -0.0115 | — | 3 |
| 1 | 30 | 0.0178 | 0.0296 | -0.0089 | — | 0 |
| 2 | 30 | 0.0175 | 0.0332 | -0.0120 | — | 22 |
| 3 | 30 | 0.0177 | 0.0223 | -0.0148 | — | 26 |
| 4 | 30 | 0.0193 | 0.0231 | -0.0141 | — | 15 |
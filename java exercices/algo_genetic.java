public class algo_genetic {
    public static void main(String [] arg)
    {
        String target = "Trouver MOI";
        int maxPop = 100;
        String [] pop = new String[maxPop];
        double mutation_rate = 0.01;
        int maxGeneration = 1000;

        pop = init(pop, target);
        for (int gen = 1; gen < maxGeneration + 1; gen++)
        {
            System.out.println(gen);
            if (isFinish(pop, target))
            {
                System.out.println("Finish generation "+ gen + " by " + target);
                break;
            } else {
                double [] fitness = get_fitness(pop, target);
                printBest(pop, fitness, target);
                pop = newGeneration(pop, fitness, mutation_rate);
            }
        }
    }

    public static void printBest(String [] pop, double [] fitness, String target )
    {
        int indexBest = 0;
        double maxFitness = 0;

        for (int i = 0; i < fitness.length; i++) {
            if (fitness[i] > maxFitness) {
                maxFitness = fitness[i];
                indexBest = i;
            }
        }

        System.out.println("Best is " + pop[indexBest] + " with " + maxFitness);
    }

    public static boolean isFinish(String [] pop, String target)
    {
        boolean isEnd = false;
    
        for(String ADN : pop)
        {
            if(ADN.equals(target))
            {
                isEnd = true;
                break;
            }
        }
        return isEnd;
    }

    public static String[] init (String[] pop, String target)
    {
        String charactere = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890 ,.-_:;+\"*ç%&/()=?";

        for (int i = 0; i < pop.length; i++ )
        {
            char [] newADN = new char[target.length()];
            for (int j = 0; j < target.length(); j++)
            {
                int index = (int) Math.floor(Math.random() * charactere.length());
                newADN[j] = charactere.charAt(index);
            }
            pop[i] = new String(newADN);
        }
        return pop;
    }

    public static double [] get_fitness(String [] pop, String target)
    {
        double [] fitness = new double[pop.length];
        for (int i = 0; i < pop.length; i++)
        {
            double cur_fitness = 0;
            for (int j = 0; j < target.length(); j++)
            {
                if (pop[i].charAt(j) == target.charAt(j))
                {
                    cur_fitness++;
                }
            }
            cur_fitness = Math.exp(cur_fitness);
            fitness[i] = cur_fitness;
        }
        return fitness;
    }

    public static double [] make_probability(double [] fitness)
    {
        double [] probability = new double[fitness.length];
        double sum = 0;

        for (double fit : fitness) {
            sum = sum + fit;
        }

        for (int i = 0; i < fitness.length; i++)
        {
            probability[i] = fitness[i] / sum;
        }
        //System.out.println(sum/fitness.length);
        return probability;
    }

    public static String get_parent(String [] pop, double [] probability)
    {
        String parent;

        double r = Math.random();
        int index = 0;
        while (r > 0)
        {
            r = r - probability[index];
            index++;
        }
        index--;

        parent = pop[index];

        return parent;
    }

    public static String [] make_childs(String parent1, String parent2,double mutation_rate)
    {
        String [] childs = new String[2];

        int r = (int) Math.floor(Math.random() * parent1.length());
        childs[0] = parent1.substring(0, r) + parent2.substring(r);
        childs[1] = parent2.substring(0, r) + parent1.substring(r);

        return childs;
    }

    public static String make_mutation(String child, double mutation_rate)
    {
        String charactere = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890 ,.-_:;+\"*ç%&/()=?";
        char [] newChild = new char[child.length()];

        for (int i = 0; i < child.length(); i++)
        {
            if (mutation_rate > Math.random())
            {
                int randomIndex = (int) Math.floor(Math.random() * charactere.length());
                newChild[i] = charactere.charAt(randomIndex);
            } else
            {
                newChild[i] = child.charAt(i);
            }
        }
        String stringChild = new String(newChild);
        return stringChild;
    }

    public static String [] newGeneration(String [] pop, double [] fitness, double mutation_rate)
    {
        String [] newPop = new String[pop.length];
        double [] probability = make_probability(fitness);

        for (int i = 0; i < pop.length; i = i + 2)
        {
            String parent1;
            String parent2;
            do {
                parent1 = get_parent(pop, probability);
                parent2 = get_parent(pop, probability);
            } while (parent1 == parent2);
            
            String [] childs = make_childs(parent1, parent2, mutation_rate );
            String child1 = make_mutation(childs[0], mutation_rate);
            String child2 = make_mutation(childs[1], mutation_rate);

            newPop[i] = child1;
            newPop[i + 1] = child2;
        }
        return newPop;
    }
}

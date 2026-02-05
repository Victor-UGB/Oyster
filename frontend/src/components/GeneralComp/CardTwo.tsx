import Typewriter from 'typewriter-effect'
import Card from './Card'

interface Article {
  id: number
  title: string
  subTitle: string
  imgSoure: string
  para: string
}

interface CardTwoProps {
  subTitle: string
  title: string
  para: string
  colorSwitch: string
}

const CardTwo: React.FC<CardTwoProps> = ({ subTitle, title, para, colorSwitch }) => {
  const articles: Article[] = [
    {
      id: 0,
      title: "Now the world can hear from you",
      subTitle: "Share Your Best",
      imgSoure: "https://images.unsplash.com/photo-1601972605341-b039a4f3ada7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8YXBwJTIwZmVhdHVyZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60",
      para: "You can share thoughts and ideas and see how people benefit from them."
    },
    {
      id: 1,
      title: "Share your ideas in text, sound and video",
      subTitle: "The Full Experience!",
      imgSoure: "https://images.unsplash.com/photo-1520333789090-1afc82db536a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80",
      para: "Give your viewers the full experience with the text, audio and video vblogs"
    },
  ]

  return (
    <div
      className="p-8 rounded-xl transition-all duration-2000 ease-in-out"
      style={{ backgroundColor: colorSwitch, color: 'white' }}
    >
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold mb-4">{subTitle}</h2>
          {title && <h3 className="text-xl mb-4">{title}</h3>}

          <div className="text-lg leading-relaxed">
            <Typewriter
              onInit={(typewriter) => {
                typewriter
                  .typeString(para)
                  .start()
              }}
            />
          </div>
        </div>

        <hr className="w-3/4 mx-auto border-gray-400 mb-8" />

        <div className="flex gap-6 overflow-x-auto pb-4">
          {articles.map((article) => (
            <div key={article.id} className="flex-shrink-0 w-80">
              <Card
                subTitle={article.subTitle}
                title={article.title}
                para={article.para}
                actionBtn="See more"
                link="/"
                btnClass="bg-white text-gray-900 hover:bg-gray-100"
                imgSource={article.imgSoure}
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default CardTwo
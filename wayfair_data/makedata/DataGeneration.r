
library(readstata13)

## 1950 - 2005 panel data from Burke&Emrick ##
thepanel <- read.dta("us_panel.dta")

thepanel$logcornyield <- log(thepanel$cornyield)
thepanel$lower   = thepanel$dday0C 
thepanel$higher  = thepanel$dday29C

# specify the study region
usepanel <- thepanel[which(  thepanel$longitude>-100
                             & thepanel$longitude<=-82.5 
                             & thepanel$latitude>36),]

columnkeep <- c("fips","year","longitude","latitude","logcornyield","lower","higher","prec",
                "dday0C","dday5C","dday8C","dday10C","dday12C","dday15C","dday20C",
                "dday25C","dday29C","dday30C","dday31C","dday32C","dday33C","dday34C")

usepanel <- na.omit(usepanel[,which(colnames(usepanel) %in% columnkeep)])

## convert data into numeric values
indx <- sapply(usepanel, is.factor)
usepanel[indx] <- lapply(usepanel[indx], 
                         function(x) as.numeric(as.character(x)))

## drop missing values to create a complete panel  
fullspan <- expand.grid(unique(usepanel$year),unique(usepanel$fips))
colnames(fullspan)=c("year","fips")
usepanel2 <- merge(fullspan,usepanel,by=c("fips","year"),all.x=TRUE)

missing.at.least.one <- unique(usepanel2$fips[!complete.cases(usepanel2)])
usepanel3 <- usepanel2[!(usepanel2$fips %in% missing.at.least.one),]

## 2.2 add 2006-2015 new data 
#  2.2.1 Climate data pre-generated from PRISM weather data set.

datasub1 <- read.dta13("ddayByYearandFips_cropAreaWeighted1_22.dta")
datasub2 <- read.dta13("ddayByYearandFips_cropAreaWeighted23_56.dta")
data <- rbind(datasub1,datasub2)

data$lower <- data$dday0C
data$higher <- data$dday29C

data_cc <- data[,which(colnames(data) %in% columnkeep)]

# 2.2.2 Crop yield data downloaded from USDA

yield <- read.csv("corn_yield.csv",header = TRUE)
neededcounties <- read.table("oldallcounties.txt",header = TRUE)
names(neededcounties) <- "fips"
neededcounties_year <- expand.grid(neededcounties$fips,2006:2015)
names(neededcounties_year) <- c("fips","year")

yield2 <- merge(yield,neededcounties_year,
                by=c("fips","year"),all.y = TRUE)

missed =!complete.cases(yield2)
missedata <- yield2[missed,]
notmisseddata <- yield2[!missed,]


for (i in 1:sum(missed)){
  thefips <- missedata[i,1]
  theyear <- missedata[i,2]
  thestate <- floor(missedata[i,1]/1000)
  
  thecode <- notmisseddata[which(notmisseddata$fips == thefips)[1],11]
  
  therow <- which(yield$year==theyear & 
                    yield$statefips == thestate &
                    yield$Ag.District.Code == thecode &
                    yield$countyfips == 999)
  
  yield2$yield[which(missed==TRUE)[i]]=yield[therow,10]
}

# 3.2.3. Combine yield with climate

data0615 <- merge(yield2,data_cc,by=c("fips","year"),all.x = TRUE)

data0615$logcornyield <- log(data0615$yield)

# read in coords
coords <- read.table("coords.txt",header = TRUE)
data0615_f <- merge(data0615, coords, by="fips",all.x = TRUE)

data0615_f <- data0615_f[,which(colnames(data0615_f) %in% columnkeep)];head(data0615_f)
#data0615_f <- data0615_f[,c(1,2,3,7,8,6,4,5)]

newdata <- data0615_f
newdata$prec <- newdata$prec/10; head(newdata)


## 3.3 merge and add few new

dim(usepanel3);dim(newdata)
usepanel3<-usepanel3[,columnkeep]
newdata<-newdata[,columnkeep]
if(sum(names(newdata) != names(usepanel3))>0) stop("colunm names not consistent")
allPanel <- rbind(usepanel3,newdata)

summary(allPanel)
years<-as.numeric(as.character(allPanel$year))
allPanel$t <- (years-mean(years))
allPanel$t2 <- allPanel$t^2
allPanel$precsq <- (allPanel$prec)^2

write.csv(allPanel,"Paneldata.csv")


